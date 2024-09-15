from django.contrib import admin
from django.urls import path

from course import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('course/<int:id>/', views.CourseListview.as_view(), name='course'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('video/<int:pk>/detail/', views.VideoDetailView.as_view(), name='video_detail'),

    path('videos/<int:id>/', views.VideoListView.as_view(), name='videos'),
]
