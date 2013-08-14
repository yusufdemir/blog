#-*- coding: utf-8 -*-
__author__ = 'yusuf'

from django import forms
from post.models import *
from account.models import Profile


class PostForm(forms.ModelForm):

    class Meta:
        model = mPost
        fields = ['cat','title','text','tags']
        #widgets = {'user':forms.HiddenInput}


    def save(self, *args, **kwargs):
        self.instance.user = kwargs.pop('user')
        super(PostForm, self).save()

class userProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields = ['first_name','last_name','image', 'phone', 'job']

