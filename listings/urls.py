from django.urls import path #standard pathing requirement for django 

from . import views #"From all import views", views will provide the functions that will be used

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), 
    path('search', views.search, name='search'), 
]
