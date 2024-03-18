from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('testing', views.Portfolio, name = 'portfolio'),
    path('students/', views.StudentListView.as_view(), name = 'students'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name = 'student-detail'),
    path('projects/', views.ProjectListView.as_view(), name = 'projects'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name = 'project-detail'),
    path('create_Project/', views.add_project, name='create_Project'),
    path('update_Project/<str:pk>/', views.update_project, name= 'update_Project'),
    path('delete_Project/<str:pk>/', views.delete_project, name= 'delete_Project'),

]
