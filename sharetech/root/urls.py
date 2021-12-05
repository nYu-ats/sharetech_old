from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from sharetech.views import (
    login_view, top_page_view, user_create_view, user_create_done_view,
    user_create_complete_view, async_consult_window_view, keyword_search_view,
    category_filter_view, consult_window_detail_view, apply_check_view,
    apply_status_view, profile_view, profile_edit_view
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view.auth_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('top/', top_page_view.top_page, name='top'),
    path('register/', user_create_view.user_create, name='register'),
    path('register/done', user_create_done_view.user_create_done, name='register_done'),
    path('register/complete/<token>/', user_create_complete_view.user_create_complete, name='register_complete'),
    path('top/asyncLoad/', async_consult_window_view.async_consult_window_load),
    path('keyword-search/', keyword_search_view.keyword_search, name='keyword_search'),
    path('category-filter/<str:category_id>/', category_filter_view.category_filter, name='category_filter'),
    path('detail/<str:consult_window_id>', consult_window_detail_view.consult_window_detail, name='consult_window_detail'),
    path('detail/<str:consult_window_id>/applyCheck/', apply_check_view.apply_check, name='apply_check'),
    path('applyStatus/', apply_status_view.apply_status, name='apply_status'),
    path('profile/', profile_view.profile, name='profile'),
    path('profile/edit', profile_edit_view.profile_edit, name='profile_edit'),
]