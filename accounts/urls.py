from django.urls import path #standard pathing requirement for django 

from . import views #"From all import views", views will provide the functions that will be used

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'), 
    path('logout', views.logout, name='logout'), 
    path('dashboard', views.dashboard, name='dashboard'), 
]
