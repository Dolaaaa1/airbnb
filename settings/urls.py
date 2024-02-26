from django.urls import path
from .views import *


app_name = 'settings'

urlpatterns = [
    path('',home , name='home'),
    path('search',home_search , name='home_search'),
    path('contact-us',contact_us,name='contact_us'),
    path('dashboard/',dashboard,name='dashboard'),
    path('newsletter/',news_letter_subscribe , name='newsletter'),
    path('category/<slug:category>',category_filter , name='category_filter'),
]
