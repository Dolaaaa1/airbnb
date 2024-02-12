from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_post = Post.objects.all()
    data = PostSerializer(all_post ,many=True, context={'request':request}).data
    return Response({'data':data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request,id):
    post = get_object_or_404(Post, id=id)
    data = PostSerializer(post).data
    
    return Response({'data':data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_search_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    data = PostSerializer(posts ,many=True).data
    return Response({'data':data})