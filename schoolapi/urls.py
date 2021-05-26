from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('teacher', views.Teacher_List_view)
router.register('student', views.Student_List_view)
router.register('principal', views.Principal_List_view)

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/',obtain_auth_token),
]
