from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



app_name = 'core'
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns =[
    path('api/', include(router.urls)),
 
    path('', views.all_tasks, name='all_tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('task/<int:task_id>/info/', views.task_info, name='task_info'),
    path('task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]