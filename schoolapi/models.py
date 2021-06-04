from uuid import uuid4
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(verbose_name= 'email',max_length= 60,unique= True)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login",auto_now='True')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_token = models.CharField(max_length=80,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField(unique='True')
    city = models.CharField(max_length=20)


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    guid = models.CharField(max_length=40, default=uuid4().hex)
    qualification = models.CharField(max_length=15, blank=True, null=True)
    primary_subject = models.CharField(max_length=20, blank=True, null=True)
    secondary_subject = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.guid = uuid4().hex if not self.guid else self.guid
        super(Teacher, self).save(*args, **kwargs)


class Principal(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
