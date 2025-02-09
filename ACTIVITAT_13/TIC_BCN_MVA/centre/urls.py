from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.profe, name='profe'),
    path('students/', views.alumn, name='alumn'),

    path('profes/profe/<str:pk>/', views.profe_datos, name='profe_datos'),
    path('profes/', views.index_profe, name='index_profe')

    path('', views.index, name='index'),
    path('profes_alumnes/<str:pk>/', views.alumn_profe, name='alumn_profe')
    path('', views.index, name='index')
]