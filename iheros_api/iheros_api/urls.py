from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/register', UserCreate.as_view(), name='Register'),
    path('account/auth', obtain_auth_token, name='Authenticate'),
]
