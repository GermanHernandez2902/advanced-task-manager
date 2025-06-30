from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_project, name='create_project'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/update_status/', views.task_update_status, name='task_update_status'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('projects/', views.project_list, name='project_list'),


]
