from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . models import Student,Teacher,Principal, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Principal)
admin.site.register(Student)