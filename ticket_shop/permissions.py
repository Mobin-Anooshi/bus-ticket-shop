from rest_framework.permissions import BasePermission,SAFE_METHODS
from accounts.models import User
from django.shortcuts import get_object_or_404


class IsDriverOnly(BasePermission):
    def has_permission(self, request, view):
        user = get_object_or_404(User , pk=request.user.id)
        return user ==request.user  and request.user.is_authenticated or request.user.is_superuser