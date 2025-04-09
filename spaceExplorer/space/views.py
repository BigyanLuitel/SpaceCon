from django.shortcuts import render, get_object_or_404
from .models import celestialBodies
from .models import blogs
import requests
# Create your views here.
def home(request):
    blogPost=blogs.objects.all()
    return render(request,'space/home.html',{'Blogs':blogPost})

def celestial_list(request):
    celestial_bodies=celestialBodies.objects.all()
    return render(request, 'space/celestial_list.html', {'celestial_bodies': celestial_bodies})

def blog_detail(request, blog_id):
    blog = get_object_or_404(blogs, id=blog_id)
    popular_posts = blogs.objects.exclude(id=blog_id).order_by('-views')[:3]
    return render(request, 'space/blog_details.html', {
        'blog': blog,
        'popular_posts': popular_posts
        
        })


def weather_view(request):
    city = "Kathmandu"
    api_key = '94324187f88140a389683737250604'
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    weather_data = response.json() if response.status_code == 200 else None

    return render(request, 'space/weather.html', {'weather': weather_data})

def APOD_view(request):
    DEMO_KEY='TlrOrMPJlghiLPFjYwwcDp3KzCVBl2eDrq9sNn6D'
    url=f"https://api.nasa.gov/planetary/apod?api_key={DEMO_KEY}"
    response=requests.get(url)
    APOD_data=response.json() if response.status_code == 200 else None
    return render(request,'space/APOD.html',{'APOD':APOD_data})