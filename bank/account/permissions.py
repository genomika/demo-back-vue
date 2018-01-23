from rest_framework import permissions
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication


class IsUserAccountOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # check if user is owner
        return request.user == obj.profile.user


class JSONWebTokenAuthenticationQS(BaseJSONWebTokenAuthentication):
    def get_jwt_value(self, request):
        print('entrou aqui')
        return request.QUERY_PARAMS.get('jwt')