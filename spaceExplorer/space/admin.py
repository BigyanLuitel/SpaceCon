from django.contrib import admin

# Register your models here.
from .models import celestialBodies
admin.site.register(celestialBodies)
list_display = ('name', 'description')

from .models import blogs
admin.site.register(blogs)
display=('name','description')