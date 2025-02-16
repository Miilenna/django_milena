from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name='login_form'),
    path('sense_sessio/', views.login_sense_sessio, name='login_sense_sessio'),
    path('inici/', views.inici, name='inici'),
    path('logout/', views.logout_view, name='logout'),
]
