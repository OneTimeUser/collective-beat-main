from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import CustomEmailUser


class MyCustomEmailUserAdmin(EmailUserAdmin):
    pass

admin.site.register(CustomEmailUser, MyCustomEmailUserAdmin)