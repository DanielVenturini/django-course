from django.urls import path

from . import views

urlpatterns = [
    path('time/', views.time_viewer, name='time'),
    path('disk-usage/', views.disk_usage_viewer, name='disk-usage'),
    path('run/<str:command>', views.run_command_viewer, name='generic-command'),
]