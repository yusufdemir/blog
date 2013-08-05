#-*- coding: utf-8 -*-
__author__ = 'yusuf'

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import *


class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ( "username", "email" , "first_name", "last_name")
