from users.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/teachers/', null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    duration = models.TimeField(null=True, blank=True)
    file = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    text = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
