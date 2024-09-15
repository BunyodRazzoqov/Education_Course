import os
import json
from datetime import datetime

from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from course.models import Category, Course, Video
from config.settings import EMAIL_DEFAULT_SENDER, BASE_DIR
from users.models import User


@receiver(post_save, sender=Course)
def post_save_customer(sender, instance, created, *args, **kwargs):
    if created:
        subject = 'Course Created'
        message = f'{instance.name} was created successfully.'
        from_email = EMAIL_DEFAULT_SENDER
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False
        )


post_save.connect(post_save_customer, sender=Course)


@receiver(post_save, sender=Category)
def post_save_customer(sender, instance, created, *args, **kwargs):
    if created:
        subject = 'Category Created'
        message = f'{instance.title} was created successfully.'
        from_email = EMAIL_DEFAULT_SENDER
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False
        )


post_save.connect(post_save_customer, sender=Category)


@receiver(post_save, sender=Video)
def post_save_customer(sender, instance, created, *args, **kwargs):
    if created:
        subject = 'Added a new video'
        message = f'{instance.title} was created !'
        from_email = EMAIL_DEFAULT_SENDER
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False
        )


post_save.connect(post_save_customer, sender=Video)


@receiver(pre_delete, sender=Video)
def save_deleted_customer(sender, instance, *args, **kwargs):
    current_date = datetime.date(datetime.now())
    current_date1 = str(current_date)

    filename = os.path.join(BASE_DIR, 'course/video_data', f'{instance.title}-{current_date1}.json')
    customer_data = {
        'title ': instance.title,
        'course': str(instance.course),
        'video': instance.file.url,

    }
    with open(filename, mode='w') as f:
        json.dump(customer_data, f, indent=4)

    print('Video successfully deleted')
