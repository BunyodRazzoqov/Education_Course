import os

from django.db.models import Avg, Sum, Count

from config.settings import BASE_DIR
from django.views.generic import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from django.shortcuts import render, get_object_or_404, redirect
from typing import Optional
from course.models import Course, Category, Teacher, Video, Comment
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor
from course.forms import CommentForm


# Create your views here.


class HomeView(View):
    template_name = 'course/index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        context = {'categories': categories, 'courses': courses, 'teachers': teachers}
        return render(request, self.template_name, context)


class CategoryListView(View):
    model = Category
    context_object_name = 'categories'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'course/base/base.html', context)


class TeacherListView(ListView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        context = {'categories': categories, 'teachers': teachers}
        return render(request, 'course/teacher.html', context)


class CourseListview(View):
    template_name = 'course/course.html'

    def get(self, request, id: Optional[int] = None):
        categories = Category.objects.all()
        if id == 0 or id is None:
            courses = None
        else:
            courses = Course.objects.filter(category__id=id)
        popular_courses = Course.objects.filter(price__gte=0).order_by('-price')[:10]
        if courses:
            for course in courses:
                course.average_rating = Comment.objects.filter(video_id__course_id=course).aggregate(Avg('rating'))[
                    'rating__avg']

        context = {'categories': categories, 'courses': courses, 'popular_courses': popular_courses}
        return render(request, self.template_name, context)


class VideoListView(LoginRequiredMixin, View):
    def get(self, request, id):
        videos = Video.objects.filter(course__id=id)
        categories = Category.objects.all()
        for video in videos:
            video.average_rating = Comment.objects.filter(video_id=video).aggregate(Avg('rating'))['rating__avg']
        context = {'videos': videos, 'categories': categories}
        return render(request, 'course/videos.html', context)


def about(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'course/about.html', context)



class VideoDetailView(DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'course/video_detail.html'

    def post(self, request, *args, **kwargs):
        video = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user
            comment.save()
            return redirect('home')
        return self.get(request, *args, **kwargs)


