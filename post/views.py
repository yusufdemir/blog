# Create your views here.
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from post.forms import *


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


def index(request):
    post = mPost.objects.all()
    ctx = {'post': post}
    return render(request, 'index.html', ctx)


def catview(request, cat_id):
    post = mPost.objects.filter(mPost.cat.pk == cat_id)
    ctx = {
        'post': post
    }
    return render(request, 'categories.html', ctx)
