from django.db import models
from django.utils import timezone

# Create your models here.

class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=300)
    fb_link  = models.URLField( max_length=200)
    twitter_link  = models.URLField( max_length=200)
    instagram_link  = models.URLField( max_length=200)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.site_name
    
    
    
class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now())  
    
    class Meta:
        verbose_name = ("Newsletter")
        verbose_name_plural = ("Newsletter")
        
        
    def __str__(self):
        return self.email    
