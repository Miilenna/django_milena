from django.urls import path
from . import views

urlpatterns = [
    path('user-form/', views.user_form, name='user_form'),
    path('', views.inici, name='inici')
]