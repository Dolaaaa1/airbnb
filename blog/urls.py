from django.urls import path
from . import views
from .api_view import post_list_api ,post_detail_api ,post_search_api


app_name = 'blag'

urlpatterns = [
    path('',views.PostList.as_view(),name='post_list'),
    path('<slug:slug>',views.PostDetail.as_view(),name='post_detail'),
    path('category/<str:slug>',views.PostsByCategory.as_view(),name='post_by_category'),
    path('tags/<slug:slug>',views.PostsByTags.as_view(),name='post_by_tags'),
    
    ##api
    path('api/list/',post_list_api,name="post_list_api"),
    path('api/list/<int:id>',post_detail_api,name='post_detail_api'),
    path('api/list/filter/<str:query>',post_search_api,name='post_search_api'),
]
