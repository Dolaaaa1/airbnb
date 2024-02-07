from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('reservation/',views.my_reservation,name='reservation'),
    path('mylisting/',views.my_listing,name='mylisting'),
    path('profile/edit',views.edit_profile,name='profile_edit')
    
]