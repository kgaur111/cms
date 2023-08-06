from rest_framework.permissions import BasePermission
class IsBlogPublicOrAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET request if the blog is public
        if request.method == 'GET' and obj.is_public:
            return True

        # Allow PUT and DELETE requests if the user is the author of the blog
        return obj.Author == request.user