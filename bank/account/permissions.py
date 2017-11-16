from rest_framework import permissions


class IsUserAccountOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # check if user is owner
        return request.user == obj.profile.user
