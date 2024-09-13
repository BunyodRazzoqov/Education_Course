from django.views.generic import View
from django.views.generic import ListView

from django.shortcuts import render

from course.models import Course, Category, Teacher


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
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'course/teacher.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        teachers = self.get_queryset()
        context['teachers'] = teachers

        return context


class CourseListview(View):
    template_name = 'course/course.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        courses = Course.objects.all()
        context = {'categories': categories, 'courses': courses}
        return render(request, self.template_name, context)
