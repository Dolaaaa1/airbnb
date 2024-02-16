from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    auther =models.ForeignKey(User,related_name='post_auther', on_delete=models.CASCADE, verbose_name=_('author'))
    title = models.CharField(max_length=200, verbose_name =_('title'))
    tags = TaggableManager()
    image = models.ImageField(_('image'),upload_to='post/') 
    created_at =models.DateTimeField(_('created at'),default=timezone.now) 
    description = models.TextField(_('description'),max_length=15000)
    category =models.ForeignKey("Category",related_name='post_category', on_delete=models.CASCADE,verbose_name=_('category'))
    slug = models.SlugField(_('url'),null= True,blank=True)  
    
    def save(self, *args, **kwargs):
       if not self.slug:
         self.slug = slugify(self.title)
       super(Post, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return self.title   
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
       
    
    
class Category(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name   