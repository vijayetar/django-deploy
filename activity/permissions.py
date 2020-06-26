from rest_framework import permissions

class IsEventUserOrReadOnly(permissions.BasePermission):
  def has_user_permission(self,request,view,obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.event_user==request.user
  