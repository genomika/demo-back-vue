"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework_jwt import views
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.contrib import admin


# Serializers define the API representation.
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from account.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'^api/v1/users', UserViewSet)

class UserTokenView(RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        user = self.request.user
        if user:
            return user
        return super(UserTokenView, self).get_object(self, queryset)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     print(kwargs)
    #     print(request.POST)
    #     token = kwargs.get('token', None)
    #     # serializer = self.serializer_class(request.user, request)
    #     # if serializer.is_valid():
    #     #     return Response(serializer.data, status=status.HTTP_200_OK)
    #     # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    #
    #     if request.user:
    #         serializer.is_valid()
    #         return Response(UserSerializer(request.user).data)
    #     return super(UserView, self).retrieve(self, request, *args, **kwargs)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('account.urls', namespace='api')),
    url(r'^api/v1/auth/login', views.obtain_jwt_token),
    url(r'^api/v1/auth/verify', views.verify_jwt_token),
    url(r'^api/v1/auth/refresh', views.refresh_jwt_token),
    url(
        r'^api/v1/auth/user',
        UserTokenView.as_view(),
        name='user-detail'
    ),
]
