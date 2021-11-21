from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from sharetech.views import (
    login_view, top_page_view, user_create_view, user_create_done_view,
    user_create_complete_view, async_consult_window_view
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view.auth_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', top_page_view.top_page, name='top'),
    path('register/', user_create_view.user_create, name='register'),
    path('register/done', user_create_done_view.user_create_done, name='register_done'),
    path('register/complete/<token>/', user_create_complete_view.user_create_complete, name='register_complete'),
    path('asyncLoad/', async_consult_window_view.async_article_load),
]
