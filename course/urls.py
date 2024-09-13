from django.contrib import admin
from django.urls import path

from course import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('course/', views.CourseListview.as_view(), name='course'),
]
