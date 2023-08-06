from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from CMS.permission import IsBlogPublicOrAuthor
from .models import User, Blog, Like
from .serializers import UserSerializer, BlogSerializer, LikeSerializer
# from Practical_task.settings import IsOwnerOrPublicOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from CMS.models import Like

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsBlogPublicOrAuthor]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    
    serializer_class = LikeSerializer

# '''
# Url:"/posts/{postid}/likes
# '''
def post_likes(request, blog_id):
        blog = get_object_or_404(Blog, Id=blog_id)
        likes = Like.objects.filter(Post_Id=blog_id)
        
        likes_data = [{'user': like.User_Id.Name,'created_on':like.Liked_On } for like in likes] # user in zip(likes, liked_users)]

        response_data = {
        'post_title': blog.Title,
        'post_Id': blog.Id,
        'post_description':blog.Description,
        'post_content':blog.Content,
        'likes': likes_data,
         }
        return JsonResponse(response_data, safe=False)

