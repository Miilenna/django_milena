from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.profe, name='profe'),
    path('students/', views.alumn, name='alumn'),
    path('', views.index, name='index'),
    path('profes_alumnes/<str:pk>/', views.alumn_profe, name='alumn_profe')
    path('', views.index, name='index')
]