from django.urls import path
from . import views
from .views import weather_view
from .views import APOD_view
urlpatterns = [
    path('',views.home,name='home'),
    path('Planets/',views.celestial_list,name='celestial_list'),
    path('weather/', weather_view, name='weather'),
     path('apod/', APOD_view, name='apod'),
]