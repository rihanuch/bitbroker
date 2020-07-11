from rest_framework import permissions


class IsOwner(permissions.IsAuthenticated):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # instance must belong to user
        return obj.user == request.user


class IsUser(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj == request.user
