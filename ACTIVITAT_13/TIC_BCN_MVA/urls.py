from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('prova/', include('prova.urls')),
    path('admin/', admin.site.urls),
]