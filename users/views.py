import jwt, requests

from django.http  import JsonResponse
from django.views import View

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM


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

        access_token = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm = ALGORITHM)

        return JsonResponse({'access_token' : access_token}, status = 200 )

    except KeyError:
      return JsonResponse({"message": "KEY_ERROR"}, status = 400)
      
    except ValueError:
      return JsonResponse({'message' : 'INVALID_ERROR'}, status = 400)
