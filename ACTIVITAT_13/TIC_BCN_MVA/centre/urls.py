from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.index, name='index')
]