from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/add/', views.TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:task_id>/edit/', views.TaskEditView.as_view(), name='task_edit'),
]
