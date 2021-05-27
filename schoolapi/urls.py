from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="School API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('teacher', views.Teacher_List_view)
router.register('student', views.Student_List_view)
router.register('principal', views.Principal_List_view)

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/',obtain_auth_token),
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
