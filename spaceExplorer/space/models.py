from django.db import models

# Create your models here.
class celestialBodies(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="space/images",default="")
    
    def __str__(self):
        return self.name
class blogs(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="space/images",default="")
    
    def __str__(self):
        return self.name