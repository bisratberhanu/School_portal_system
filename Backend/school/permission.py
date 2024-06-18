from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.permissions import SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        print("------------------------------------")
        if request.user and request.user.is_authenticated:
            print("===============================")
            print(request.user.role)
            return request.user.is_staff or request.user.role == 'A'
        
        return False