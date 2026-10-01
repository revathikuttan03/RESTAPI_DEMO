from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('tasksviewset', views.TaskViewSet)

urlpatterns = [
    path('tasks/', views.task_list,),
    path('tasks/<int:pk>/', views.task_detail,),

    path('tasksapi/', views.TaskListAPI.as_view(),),
    path('tasksapi/<int:pk>/', views.TaskDetailAPIView.as_view(),),

    path('tasksgeneric/', views.TaskListGenericView.as_view(),),
    path('tasksgeneric/<int:pk>/', views.TaskDetailGenericView.as_view(),),
    path('', include(router.urls)),
]