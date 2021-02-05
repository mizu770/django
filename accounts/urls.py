from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login' ),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout' ),
    path('register/', register, name='register'),
]


#http://127.0.0.1:8000/accounts/profile/

# 위 페이지 처리방법

# 1. profile 페이지를 작성

# 2. profile 페이지가 아닌 다른 페이지로 보내기
    # - 장고 설정 변경

    # - 웹 서버에서 설정 (redirect)