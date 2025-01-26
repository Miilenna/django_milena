from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.index, name='profe'),
    path('students/', views.index, name='alumn')
]