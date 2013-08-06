from django.utils.translation import ugettext

__author__ = 'yusuf'
from post.models import mCategories
def categories(request):
    cat = mCategories.objects.all()
    return {'cat': cat}

def loginForm(request):
    form = ugettext("Login")
    return {'loginform':form}