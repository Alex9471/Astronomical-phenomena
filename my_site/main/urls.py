from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('blackout', views.blackout),
    path('about_project', views.about_project),
    path('comets', views.comets),
    path('polar_lights', views.polar_lights),
]
