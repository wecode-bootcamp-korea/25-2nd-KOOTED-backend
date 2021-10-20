import json, jwt, requests

from django.http  import JsonResponse
from django.views import View
from django.db    import transaction

from users.models import User
from posts.models import UserWorkingYear
from my_settings  import SECRET_KEY, ALGORITHM
from kooted.utils import login_decorator
 

class KakaoSignInView(View):
  def get(self,request):
    try:
        kakao_token = request.headers.get('Authorization')
        headers     = {'Content-Type': 'application/json; charset=utf-8', 'Authorization' : f'Bearer {kakao_token}'}
        response    = requests.get('https://kapi.kakao.com/v2/user/me', headers = headers).json()
        kakao_id    = response['id']
        email       = response['kakao_account']['email']
        name        = response['kakao_account']['profile']['nickname']

        user, created = User.objects.get_or_create(
            kakao_id  = kakao_id,
            email     = email,
            name      = name
        )

        access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = ALGORITHM)

        if not user.salary:
            return JsonResponse({'message' : 'NOT_ENOUGH_INFORMATION', 'access_token' : access_token}, status = 200)

        return JsonResponse({'message' : 'SUCCESS', 'access_token' : access_token}, status = 200 )

    except KeyError:
      return JsonResponse({"message": "KEY_ERROR"}, status = 400)
      
    except ValueError:
      return JsonResponse({'message' : 'INVALID_ERROR'}, status = 400)

class UserView(View):
    @login_decorator
    def get(self, request):
        try:
            user = request.user
            user_info = {
                'id' : user.id,
                'name' : user.name,
                'email' : user.email,
                'mobile_number' : user.mobile_number,
                'applications' : user.application_set.count(),
                'bookmarks' : [{'id' : bookmark.post.id,
                                'title' : bookmark.post.title,
                                'company_name' : bookmark.post.company.name,
                                'location' : bookmark.post.company.location,
                                'image_url' : bookmark.post.postimage_set.first().image_url if bookmark.post.postimage_set.first() else None}
                                for bookmark in user.bookmark_set.select_related('post').all()]
            }

            return JsonResponse({'message' : 'SUCCESS', 'user_info' : user_info}, status = 200)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'USER_DOES_NOT_EXIST'}, status = 400)
            
    @login_decorator
    def put(self, request):
        try:
            user = request.user
            data = json.loads(request.body)
            with transaction.atomic():
                User.objects.filter(id=user.id).update(
                    salary = data['salary'],
                )

                if not UserWorkingYear.objects.filter(user=user).exists():
                    UserWorkingYear.objects.create(
                        job_id = data['job_id'],
                        working_year_id = data['working_year'] + 1,
                        user = user
                    )

                else:
                    UserWorkingYear.objects.filter(user=user).update(
                        job_id = data['job_id'],
                        working_year_id = data['working_year'] + 1,
                        user = user
                    )

            return JsonResponse({'message' : 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)