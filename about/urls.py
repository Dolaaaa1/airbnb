from django.urls import path
from .views import AboutView

app_name = 'abut'
urlpatterns = [
    path('',AboutView.as_view(),name='about')
]
