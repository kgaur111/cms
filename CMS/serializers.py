from rest_framework import serializers
from CMS.models import User,Blog,Like

#Company serialziers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields= "__all__" # include all the fields of User model


class AuthorField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        try:
            Id = int(data)
            return User.objects.get(pk=Id)
        except (TypeError, ValueError, User.DoesNotExist):
            raise serializers.ValidationError("Invalid Author ID")
        
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    likes_count = serializers.SerializerMethodField()
    Author = AuthorField(queryset=User.objects.all(), default=1)
    class Meta:
        model = Blog
        fields= "__all__" # include all the fields of Post model

    def get_likes_count(self, obj):
        return Like.objects.filter(Post_Id=obj).count()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.is_public or instance.Author == self.context['request'].user:
            return data
    # For private posts, hide content and other details
        data['content'] = "This is a private post."
        # You can add more fields to hide as needed
        return data

class BlogField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        try:
            Id = int(data)
            return Blog.objects.get(pk=Id)
        except (TypeError, ValueError, User.DoesNotExist):
            raise serializers.ValidationError("Invalid Blog ID")


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    Post_Id = BlogField(queryset=Blog.objects.all(), default=1)
    User_Id = AuthorField(queryset=User.objects.all(), default=1)
    
    class Meta:
        model = Like
        fields= "__all__" # include all the fields of Like model

