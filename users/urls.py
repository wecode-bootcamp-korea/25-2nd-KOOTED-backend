from django.urls import path
from users.views import KakaoSignInView

urlpatterns = [
    path('/kakao', KakaoSignInView.as_view()),
]