from django.urls import path

from . import views

urlpatterns = [
    path('user-form/', views.user_form, name='user_form'),
    path('login/', views.login_form, name='login_form'),
    path('process-login/', views.process_login, name='process_login'),
    path('login-error/', views.login_error, name='login_error'),
    path('', views.inici, name='inici')
]