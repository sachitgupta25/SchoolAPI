from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacher', views.Teacher_List_view)
router.register('student', views.Student_List_view)
router.register('principal', views.Principal_List_view)

urlpatterns = [
    path('', include(router.urls)),
]
