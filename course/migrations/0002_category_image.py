# Generated by Django 5.1.1 on 2024-09-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='123', upload_to='images/categories/'),
            preserve_default=False,
        ),
    ]
