from django.urls import path #standard pathing requirement for django 

from . import views #"From all import views", views will provide the functions that will be used

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
]
