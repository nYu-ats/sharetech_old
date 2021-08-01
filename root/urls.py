"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from sharetech.views import (
    LoginView, testView, UserCreateView, UserCreateDoneView,
    UserCreateCompleteView, 
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.auth_login, name='login'),
    path('', testView.testRouteView, name='top'),
    path('register/', UserCreateView.user_create, name='register'),
    path('register/done', UserCreateDoneView.user_create_done, name='register_done'),
    path('register/complete/<token>/', UserCreateCompleteView.user_create_complete, name='register_complete'),
]
