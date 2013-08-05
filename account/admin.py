__author__ = 'yusuf'
from django.contrib import admin
from account.models import *
from post.models import *

admin.site.register(Profile)
admin.site.register(mCategories)
admin.site.register(mPost)
admin.site.register(mComment)
