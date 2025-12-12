from django.urls import path
from django.contrib import admin
from minha_api.api import api 

urlpatterns = [
    path(f'api/', api.urls),
    path(f'admin/', admin.site.urls),
]