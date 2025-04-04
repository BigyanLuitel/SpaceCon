from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('celestial/',views.celestial_list,name='celestial_list'),
]