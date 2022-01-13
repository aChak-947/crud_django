from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.addStudent, name="add-student"),
    path('update/<str:pk>/', views.updateStudent, name="update-student"),
    path('delete/<str:pk>/', views.deleteStudent, name="delete-student"),
]