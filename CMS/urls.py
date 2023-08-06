from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,LikeViewSet,BlogViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs/<int:blog_id>/likes/', views.post_likes, name='post_likes')
]

