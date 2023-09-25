from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from config import config


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

API_VERSION = config.api.version

urlpatterns = [
   path(f'{API_VERSION}admin/', admin.site.urls),
   path(f'{API_VERSION}docs/', schema_view.with_ui('swagger', cache_timeout=0)),

   path(f'{API_VERSION}token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path(f'{API_VERSION}token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path(f'{API_VERSION}token/verify/', TokenVerifyView.as_view(), name='token_verify'),

   path(f'{API_VERSION}task/', include('src.tasks.urls')),
   path(f'{API_VERSION}user/', include('src.users.urls')),
]
