#-*- coding: utf-8 -*-
__author__ = 'yusuf'

from django import forms
from account.models import *
from post.models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = mPost
