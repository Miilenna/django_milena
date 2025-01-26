from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.profe, name='profe'),
    path('students/', views.alumn, name='alumn')
]