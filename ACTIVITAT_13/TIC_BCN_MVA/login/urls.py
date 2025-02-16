from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_form, name='login_form'),
    path('process_login/', views.process_login, name='process_login'),
    path('', views.inici, name='inici'),
    path('logout/', views.logout, name='logout'),
]
