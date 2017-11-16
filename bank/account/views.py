# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Profile, BankAccount
from .serializers import ProfileSerializer, BankAccountSerializer
from .permissions import IsUserAccountOwner


class ProfileListCreateAPIView(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser,)


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'cpf'
    permission_classes = (IsAdminUser,)


class BankAccountListCreateAPIView(generics.ListCreateAPIView):

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = (IsUserAccountOwner,)


class BankAccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = (IsUserAccountOwner,)
    lookup_field = 'account_number'
