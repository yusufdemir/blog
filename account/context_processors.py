__author__ = 'yusuf'
from post.models import mCategories
def categories(request):
    cat = mCategories.objects.all()
    return {'cat': cat}

def loginForm(request):
    form = "test form text"
    return {'loginform':form}