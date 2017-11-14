from django.conf.urls import url
from account import views as api_views


urlpatterns = [
    url(
        r'^profile/$',
        api_views.ProfileListCreateAPIView.as_view(),
        name='profile-list'
    ),
    url(
        r'^profile/(?P<cpf>([A-Za-z0-9\-_]+))/$',
        api_views.ProfileRetrieveUpdateDestroyAPIView.as_view(),
        name='profile-detail'
    ),
    url(
        r'^bankaccount/$',
        api_views.BankAccountListCreateAPIView.as_view(),
        name='bankaccount-list'
    ),
    url(
        r'^bankaccount/(?P<account_number>([A-Za-z0-9\-_]+))/$',
        api_views.BankAccountRetrieveUpdateDestroyAPIView.as_view(),
        name='bankaccount-detail'
    ),
]
