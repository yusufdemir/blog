# Create your views here.
from django.contrib.auth import logout
from django.core.context_processors import request
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, check_password
from forms import SignUpForm
from random import choice
from string import letters


def logout_view(self):
    logout(request('/index/'))

class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



def test(request):
    test = "asdasd"
    return render_to_response("index.html", {'test': 'testtext'},
                              context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        data = request.POST.copy() # so we can manipulate data

        # random username
        data['username'] = ''.join([choice(letters) for i in xrange(30)])
        form = SignUpForm(data)

        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/sign_up_success.html')
    else:
        form = SignUpForm()

    return render_to_response('login.html', {'form':form},
                              context_instance=RequestContext(request))


