from django.urls import path
from users.views import KakaoSignInView, UserView

urlpatterns = [
    path('/kakao', KakaoSignInView.as_view()),
    path('', UserView.as_view()),
]
