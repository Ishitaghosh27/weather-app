from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage with weather search
    path('city-suggestions/', views.city_suggestions, name='city_suggestions'),
]
