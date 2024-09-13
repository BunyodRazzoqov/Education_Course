from django.contrib import admin
from users.models import User
from import_export.admin import ImportExportModelAdmin


# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email', 'username')
