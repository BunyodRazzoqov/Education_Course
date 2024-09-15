from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe

from course.models import Course, Teacher, Category, Video,Comment


# Register your models here.

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'teachers', 'preview_image')
    search_fields = ('name', 'category')
    list_filter = ('category',)

    def preview_image(self, obj):
        if obj.image.url:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 30px;">')

    preview_image.short_description = 'Image'


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'full_name', 'preview_image')

    def preview_image(self, obj):
        if obj.image.url:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 30px;">')

    preview_image.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'preview_image')

    def preview_image(self, obj):
        if obj.image.url:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 30px;">')

    preview_image.short_description = 'Image'


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'course__id', 'course')


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'video')
