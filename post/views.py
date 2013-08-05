# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from post.forms import *
from post.models import *

@login_required
def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            form.save()
            return HttpResponseRedirect('/kayittamam/')
        return render_to_response("sendpost.html", {'form':PostForm},
                                  context_instance=RequestContext(request))
    form = PostForm()
    return render(request, "sendpost.html", {'form': form})


def index(request):
    post = mPost.objects.all()
    subcomment = mComment.objects.filter()
    ctx = {'post': post,'sub':subcomment}
    return render(request, 'index.html', ctx)

