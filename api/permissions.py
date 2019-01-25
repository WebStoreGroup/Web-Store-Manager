from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS
)

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return str(request.user) == "auth0.5c457f97a117272e332b9a20"

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user != AnonymousUser
        except:
            return False