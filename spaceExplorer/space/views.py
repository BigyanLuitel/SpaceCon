from django.shortcuts import render
from .models import celestialBodies
from .models import blogs
# Create your views here.
def home(request):
    blogPost=blogs.objects.all()
    return render(request,'space/home.html',{'Blogs':blogPost})

def celestial_list(request):
    celestial_bodies=celestialBodies.objects.all()
    return render(request, 'space/celestial_list.html', {'celestial_bodies': celestial_bodies})