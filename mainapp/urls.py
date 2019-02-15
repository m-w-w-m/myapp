from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('a', views.a, name='a'),
]
