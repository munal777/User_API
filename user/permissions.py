from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    
        if not request.user.is_anonymous:
            return request.user == obj   #If the user is logged in, they can only access the object if they own it
        return False        