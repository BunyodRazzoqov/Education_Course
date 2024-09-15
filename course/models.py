from users.models import User
from django.db import models
from datetime import timedelta


# Create your models here.


class Category(models.Model):
    title: str = models.CharField(max_length=100)
    image: str = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name: str = models.CharField(max_length=100)
    image: str = models.ImageField(upload_to='images/teachers/', null=True, blank=True)
    telegram_url: str = models.URLField(null=True, blank=True)
    instagram_url: str = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    name: str = models.CharField(max_length=100)
    description: str = models.TextField()
    category: str = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    price: float = models.FloatField()
    image: str = models.ImageField(upload_to='images/', blank=True, null=True)
    teachers: str = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    # @property
    # def video_duration(self):
    #     video_duration = sum((video.duration for video in self.videos.all()), timedelta())
    #
    #     video_seconds = int(video_duration.video_seconds())
    #     hours, remainder = divmod(video_seconds, 3600)
    #     minutes, seconds = divmod(remainder, 60)
    #
    #     return f'{hours}: {minutes}: {seconds}'

    def __str__(self):
        return self.name


class Video(models.Model):
    title: str = models.CharField(max_length=100)
    course: str = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    duration: str = models.DurationField(null=True, blank=True)
    file: str = models.FileField(upload_to='videos/', null=True, blank=True)

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

    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value,
                                              null=True, blank=True)
    text: str = models.TextField()
    video: str = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user: str = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    created_at: str = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.text
