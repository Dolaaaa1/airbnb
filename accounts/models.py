from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users/')
    
    
    def __str__(self) :
        return str(self.user)
        
    
    
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)    
