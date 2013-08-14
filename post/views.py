# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from post.forms import *
from account.views import *

@login_required
def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST )
        if form.is_valid():
            form.save(user=request.user)
            return HttpResponseRedirect('/index/')
        return render_to_response("sendpost.html", {'form': form},
                                  context_instance=RequestContext(request))
    form = PostForm()
    return render(request, "sendpost.html", {'form': form})


def profileFormView(request):
    if request.method == 'POST':
        form = userProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username = request.user.username
            form.save()
            return HttpResponseRedirect('/profile/')
        return render_to_response("profile.html",{'form':form},
                                  context_instance=RequestContext(request))
    form = userProfileForm()
    return render(request,"profile.html",{'form':form})


def index(request):
    post = mPost.objects.all()
    ctx = {'post': post}
    return render(request, 'index.html', ctx)


def catview(request, cat_id):
    post = mPost.objects.filter(cat__pk = cat_id)
    ctx = {
        'post': post
    }
    return render(request, 'index.html', ctx)


def postdetailview(request, post_id):
    post = mPost.objects.filter(pk = post_id)
    ctx = {
        'post': post
    }
    return render(request, 'index.html', ctx)

@login_required()
def mypost(request):
    post = mPost.objects.filter(user__pk =request.user.id)
    ctx = {
        'post': post
    }
    return render(request, 'index.html', ctx)