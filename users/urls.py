from django.urls import path
from users import views
from django.shortcuts import render

urlpatterns = [
	path('users/', views.users, name = 'api_users_get_post_put_delete'),
	path('users/<str:name>', views.users, name = 'api_users_by_name_get_post_put_delete'),
	path('web/users/', views.web_users, name='web_users_get_post_put_delete'),
	path('web/users/<str:name>', views.web_users, name = 'web_users_get_by_name_get_post_put_delete'),
]