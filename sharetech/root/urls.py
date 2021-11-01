from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from sharetech.views import (
    LoginView, TopPageView, UserCreateView, UserCreateDoneView,
    UserCreateCompleteView, 
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.auth_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', TopPageView.topPage, name='top'),
    path('register/', UserCreateView.user_create, name='register'),
    path('register/done', UserCreateDoneView.user_create_done, name='register_done'),
    path('register/complete/<token>/', UserCreateCompleteView.user_create_complete, name='register_complete'),
    path('asyncLoad/', TopPageView.asyncArticleLoad),
]
