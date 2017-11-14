# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .models import Profile, BankAccount
from .serializers import ProfileSerializer, BankAccountSerializer


class ProfileListCreateAPIView(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'cpf'


class BankAccountListCreateAPIView(generics.ListCreateAPIView):

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


class BankAccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    lookup_field = 'account_number'
