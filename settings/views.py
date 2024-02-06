from django.shortcuts import render
from property.models import Place ,Property ,Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    categorys = Category.objects.all()
    resturant_list = Property.objects.filter(category__name ='Restaurant')[:5]
    hotels_list = Property.objects.filter(category__name ='Hotels')[:4]
    places_list = Property.objects.filter(category__name ='Places')[:4]
    recent_posts = Post.objects.all()[:4]
    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name ='Places').count()
    resturant_count = Property.objects.filter(category__name ='Restaurant').count()
    hotels_count = Property.objects.filter(category__name ='Hotels').count()
    
    
    return render(request,'settings/home.html',{
        'places':places ,
        'categorys':categorys ,
        'resturant_list':resturant_list,
        'hotels_list':hotels_list,
        'places_list':places_list,
        'recent_posts':recent_posts,
        'users_count':users_count,
        'places_count':places_count,
        'resturant_count':resturant_count,
        'hotels_count':hotels_count,
        })
    
def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    
    property_list = Property.objects.filter(
        Q(name__icontains = name) & Q(place__name__icontains = place)
    )
    
    return render(request,'settings/home_search.html',{'property_list':property_list})


def category_filter(request ,category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    
    return render(request,'settings/home_search.html',{'property_list':property_list})


def contact_us(request):
    pass