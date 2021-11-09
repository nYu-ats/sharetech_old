from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from sharetech.views import (
    login_view, TopPageView, user_create_view, UserCreateDoneView,
    UserCreateCompleteView, 
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view.auth_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', TopPageView.topPage, name='top'),
    path('register/', user_create_view.user_create, name='register'),
    path('register/done', UserCreateDoneView.user_create_done, name='register_done'),
    path('register/complete/<token>/', UserCreateCompleteView.user_create_complete, name='register_complete'),
    path('asyncLoad/', TopPageView.asyncArticleLoad),
]
