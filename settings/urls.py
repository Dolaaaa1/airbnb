from django.urls import path
from .views import *


app_name = 'settings'

urlpatterns = [
    path('',home , name='home'),
    path('search',home_search , name='home_search'),
    path('contact-us',contact_us,name='contact_us'),
    path('category/<slug:category>',category_filter , name='category_filter'),
]
