# -*- coding: utf-8 -*-

from rest_framework.authtoken.models import Token

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'Perfil'
        verbose_name_plural = u'Perfis'

    def __str__(self):
        return self.user.username


class BankAccount(models.Model):

    profile = models.ForeignKey(Profile)
    account_number = models.CharField(unique=True, max_length=100)
    agency = models.IntegerField()
    balance = models.FloatField()

    class Meta:
        verbose_name = u'Conta'
        verbose_name_plural = u'Contas'

    def __str__(self):
        return self.profile.user.username + ' - Account: ' + str(self.account_number)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)