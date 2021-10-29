from django.shortcuts import render

# Create your views here.

import json
from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction

<<<<<<< HEAD
from posts.models import Post
=======
from posts.models import Bookmark, Post
>>>>>>> ffd0cfe (Add: posts_views)
from .models      import Application, Career, Resume, Skill
from users.models import User
from kooted.utils import login_decorator

class ResumeView(View):
    @login_decorator
    def post(self, request):
        try:
            user   = request.user
            data   = json.loads(request.body)
            with transaction.atomic():
                resume = Resume.objects.create(
                    user         = user,
                    introduction = data.get('introduction'),
                    college      = data.get('college'),
                    status       = data.get('status'),
                    title        = data.get('title')
                )    
                [resume.career_set.create(
                    company_name      = career['company_name'],
                    duty              = career['duty'],
                    date_of_joining   = career.get('date_of_joining', '0000-00-00'),
                    date_of_resigning = career.get('date_of_resigning', '0000-00-00'),
                    in_office         = career['in_office']
                ) for career in data['careers']]
                [resume.skill_set.create(
                    name       = skill['name'],
                    user       = user
                )for skill in data['skills']]
                return JsonResponse({'message' : 'CREATED'}, status = 201)

        except ArithmeticError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

    @login_decorator
    def get(self, request, resume_id):
      resume = Resume.objects.filter(id=resume_id).first()
<<<<<<< HEAD
=======
      post_id = request.GET.get('post_id')
>>>>>>> ffd0cfe (Add: posts_views)
      user = request.user
      user_info = {
        'name' : user.name,
        'email' : user.email,
<<<<<<< HEAD
        'mobile_number' : user.mobile_number
=======
        'mobile_number' : user.mobile_number,
        'bookmark' : Bookmark.objects.filter(user=user, post_id=post_id).exists()
>>>>>>> ffd0cfe (Add: posts_views)
      }

      if not resume:
        return JsonResponse({'message' : 'RESUME_NOT_EXIST', 'user_info' : user_info}, status = 200)

      resume_info = {
        'id' : resume.id,
        'introduction' : resume.introduction,
        'title' : resume.title,
        'status' : resume.status,
        'careers' : [{
          'id' : career.id,
          'company_name' : career.company_name,
          'duty' : career.duty,
          'date_of_joining' : career.date_of_joining,
          'date_of_resigning' : career.date_of_resigning,
          'in_office' : career.in_office
        } for career in resume.career_set.all()],
        'college' : resume.college,
        'skills' : [{
          'name' : skill.name
        } for skill in resume.skill_set.all()]
      }
      return JsonResponse({'MESSAGE' : 'SUCCESS', 'resume_info' : resume_info, 'user_info' : user_info}, status = 200)

    @login_decorator
    def delete(self, request, resume_id):
      try:
        user = request.user
        if not Resume.objects.filter(user=user, id=resume_id).exists():
          return JsonResponse({'MESSAGE' : 'RESUME_DOSE_NOT_EXIST'}, status = 404)
        Resume.objects.get(user=user, id=resume_id).delete()
        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 200)
      except ValueError:
        return JsonResponse({'MESSAGE' : 'VALUE_ERROR'}, status = 400)
    
    @login_decorator
    def put(self, request, resume_id):
        data = json.loads(request.body)
        resume = Resume.objects.get(id=resume_id)
      
        try:
            user = request.user
            with transaction.atomic():
                Resume.objects.filter(id=resume_id).update(
                        introduction = data.get('introduction', resume.introduction),
                        college      = data.get('college', resume.college),
                        status       = data.get('status', resume.status),
                        title        = data.get('title', resume.title),
                        user         = user
                )
                [Career.objects.filter(id=career_info.id).update(
                    company_name      = career.get('company_name', career_info.company_name),
                    duty              = career.get('duty', career_info.duty),
                    date_of_joining   = career.get('date_of_joining', career_info.date_of_joining),
                    date_of_resigning = career.get('date_of_resigning', career_info.date_of_resigning),
                    in_office         = career.get('in_office', career_info.in_office),
                    resume            = resume
                ) for career, career_info in zip(data.get('careers'), resume.career_set.all())]

                Skill.objects.filter(user=user).delete()

                [Skill.objects.create(
                    name   = skill.get('name'),
                    user   = user,
                    resume = resume
                )for skill in data.get('skills')]

                return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

        except Resume.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'DOSE_NOT_EXIST'}, status = 404)

class AllResumeView(View):
    @login_decorator
    def get(self, request):
        post_id = request.GET.get('post_id')
        user = request.user
        limit = int(request.GET.get('limit', 5))
        offset = int(request.GET.get('offset', 0))
        try:
            user_info = {
                'id' : user.id,
                'name' : user.name,
                'email' : user.email, 
                'mobile_number' : user.mobile_number,
                'bookmark' : user.bookmark_set.filter(post_id=post_id).exists()
            }
            results = [{
                'id' : resume.id,
                'title' : resume.title,
                'date' : resume.updated_at,
                'status' : resume.status
            } for resume in Resume.objects.filter(user=user)[offset:limit+offset]]
            return JsonResponse({'message' : 'SUCCESS', 'user' : user_info, 'result' : results}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

class ApplicationView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            Application.objects.create(
                recommender = data['recommender'],
                user = user,
                post = Post.objects.get(id=data['post_id']),
                resume = Resume.objects.get(id=data['resume_id']),
            )

            return JsonResponse({'message' : 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)