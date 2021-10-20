import json, requests

from django.db.models.aggregates import Avg
from django.http                 import JsonResponse
from django.views                import View
from django.db.models            import Q, F, Count, Sum

from my_settings                 import REST_API
from kooted.utils                import login_decorator
from .models                     import Bookmark, Post, WorkingYear
from companies.models            import JobGroup, Job
from users.models                import User

class PostsView(View):
    def get(self, request):
        try:
            offset       = request.GET.get('offset', 0)
            limit        = request.GET.get('offset', 20)
            sorting      = request.GET.get('sort', '-created_at')
            job_group    = JobGroup.objects.filter(id=request.GET.get('job-group', 0))
            job          = Job.objects.filter(id=request.GET.get('job', 0))
            category_list= [{'id'       : job_group.id,
                             'name'     : job_group.name,
                             'image_url': job_group.image_url,
                             'job_list' : [{'id'  : job.id,
                                            'name' : job.name
                                            } 
                                            for job in job_group.job_set.all()]}
                                            for job_group in JobGroup.objects.all()]

            salary_list  = []
            user_filters = Q()
            post_filters = Q()

            if job_group or job:
                post_filters.add(Q(job__job_group=job_group.first()) | Q(job=job.first()), post_filters.AND)
                user_filters.add(Q(userworkingyear__job__job_group=job_group.first()) | Q(userworkingyear__job=job.first()), user_filters.AND)
                jobs          = Job.objects.filter(job_group=job_group.first()) if job_group else Job.objects.filter(job_group=job.first().job_group).exclude(id=job.first().id)
                category_list = list(jobs.values())
                salary_list   = User.objects.filter(user_filters)\
                                            .annotate(working_year=F('userworkingyear__working_year__years'))\
                                            .values('working_year')\
                                            .annotate(total_salary=Avg('salary'))\
                                            .exclude(working_year=None)\
                                            .order_by('working_year')

            year         = int(request.GET.get('year', 0))
            tag_list     = request.GET.getlist('tag')

            if tag_list:
                post_filters.add(Q(company__companytag__tag__in=tag_list), post_filters.AND)

            if year:
                post_filters.add(Q(working_year__lte=year), post_filters.AND)

            posts        = Post.objects.select_related('company', 'job__job_group')\
                                       .prefetch_related('postimage_set')\
                                       .filter(post_filters)\
                                       .annotate(count=Count('bookmark'), reward=F('recommender_reward') + F('applicant_reward'))\
                                       .order_by(sorting)[offset:offset+limit]

            result = [{
                'id'              : post.id,
                'title'           : post.title,
                'reward'          : post.recommender_reward + post.applicant_reward,
                'company_name'    : post.company.name,
                'created_at'      : post.created_at,
                'tag'             : [{'id'    : tag.tag.id,
                                      'name'  : tag.tag.name,
                                      'color' : tag.tag.color} for tag in post.company.companytag_set.select_related('tag').all()],
                'working_year'    : post.working_year,
                'count'           : post.count,
                'image_url'       : None if not post.postimage_set.first() else post.postimage_set.first().image_url,
            } for post in posts]

            return JsonResponse({'category_list' : category_list, 'salary_list' : list(salary_list), 'result' : result}, status = 200)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

class PostDetailView(View):
    def get(self, request, post_id):
        try:
            post   = Post.objects.get(id=post_id)
            location = post.company.location.split(',')
            headers= {'Content-Type': 'application/json; charset=utf-8', 'Authorization' : f'KakaoAK {REST_API}'}
            response = requests.get('https://dapi.kakao.com//v2/local/geo/coord2address.json?x={}&y={}'.format(location[1], location[0]), headers=headers).json()
            region = response['documents'][0]['address']['region_1depth_name'] + ' '+ response['documents'][0]['address']['region_2depth_name']
            post   = Post.objects.filter(id=post_id).annotate(region=F('company__location')).first()
            result = {
                'id'                 : post.id,
                'title'              : post.title,
                'recommender_reward' : post.recommender_reward,
                'applicant_reward'   : post.applicant_reward,
                'company_name'       : post.company.name,
                'content'            : post.content,
                'deadline'           : post.deadline,
                'tag'                : [{'id' : tag.tag.id, 
                                         'name' : tag.tag.name, 
                                         'color' : tag.tag.color} for tag in post.company.companytag_set.all()],
                'location'           : region,
                'count'              : post.bookmark_set.count(),
                'image_url'          : [{'id' : image.id, 
                                         'image_url' : image.image_url} for image in post.postimage_set.all()]
            }

            return JsonResponse({'result' : result}, status = 200)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

class BookMarkView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            if not Bookmark.objects.filter(user=user, post_id=data['post_id']).exists():
                user.bookmark_set.create(post_id=data['post_id'])

            return JsonResponse({'message' : 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_EROOR'}, status = 400)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

    @login_decorator
    def delete(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            if user.bookmark_set.get(post_id=data['post_id']):
                user.bookmark_set.get(post_id=data['post_id']).delete()

            return JsonResponse({'message' : 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_EROOR'}, status = 400)

        except Post.DoesNotExist:
            return JsonResponse({'message' : 'POST_DOES_NOT_EXIST'}, status = 400)

        except Bookmark.DoesNotExist:
            return JsonResponse({'message' : 'BOOKMARK_DOES_NOT_EXIST'}, status = 400)