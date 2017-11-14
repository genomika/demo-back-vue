from rest_framework import serializers

from .models import Profile, BankAccount


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

        fields = (
            'id',
            'user',
            'cpf'
        )

        lookup_field = 'cpf'


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount

        fields = (
            'id',
            'profile',
            'account_number',
            'agency',
            'balance'
        )

        lookup_field = 'account_number'
