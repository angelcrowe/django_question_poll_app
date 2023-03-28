from django.urls import path

from . import views

#map index view to URL 
urlpatterns = [
    path('', views.index, name='index'),
]