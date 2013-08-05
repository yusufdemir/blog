# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from account.forms import *
from account.models import Profile
from django.contrib.auth import *
import post


def test(request):
    test = "asdasd"
    return render_to_response("index.html", {'test': 'testtext'},
                              context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            form.save()
            return HttpResponseRedirect('/kayittamam/')
        return render_to_response("register.html", {'form':Registration},
                                  context_instance=RequestContext(request))
    form = Registration()
    return render(request, "register.html", {'form': form})




