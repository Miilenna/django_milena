from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.profe, name='profe'),
    path('students/', views.alumn, name='alumn'),

    path('profes/profe/<str:pk>/', views.profe_datos, name='profe_datos'),
    path('profes/', views.alumn_profe, name='index_profe'),

    path('profes_alumnes/', views.alumn_profe, name='alumn_profe'),
]