from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from helpyou.views import conversas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conversas/', conversas),
]

