from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.TaskList.as_view(), name='task_list'),
    path('sort_by_date/', views.sort_by_date, name='sort_by_date'),
    path('sort_by_priority/', views.sort_by_priority, name='sort_by_priority'),
    path('task/new/', views.TaskCreate.as_view(), name='task_new'),
    path('task/<int:pk>/edit/', views.TaskUpdate.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logoutacc, name='logout'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
]