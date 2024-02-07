from django.shortcuts import render , redirect
from .forms import SignupForm ,UserForm,ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from property.models import PropertyBook ,Property
# Create your views here.



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user =authenticate(username=username , password=password)
            login(request,user)
            
            return redirect('/accounts/profile')
        
    else:
        form = SignupForm()
    return render (request,'registration/signup.html',{'form':form})        
        


def profile(request):
    profile= Profile.objects.get(user=request.user)
    
    
    
    return render(request,'profile/profile.html',{'profile':profile})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = request.user 
            myprofile.save()
            
            return redirect('/accounts/profile')
            
        
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        
    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form ,
        'profile_form': profile_form
        
    })  
    
    
def my_reservation(request):
    property_list = PropertyBook.objects.filter(user=request.user)
    return render(request,'profile/reservation.html',{'property_list':property_list})

def my_listing(request):
    property_list = Property.objects.filter(owner=request.user)
    return render(request,'profile/mylisting.html',{'property_list':property_list}) 
