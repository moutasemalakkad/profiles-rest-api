from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to update their profile"""
    def has_object_permission(self, request, view, obj):
        """check the user who is trying to edit"""
        print('hello')
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
