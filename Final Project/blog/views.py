from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import blog
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Post




@login_required
def blog(request):
    if not request.user.is_authenticated:
        messages.warning(request, "login first please")
        return redirect("account:login")


    context = {}
    context["posts"] = Post.objects.all()
    template_name = "blog/blog.html"
    return render (request, template_name, context)


def blog_details(request, slug):
    context = {}
    post = get_object_or_404(Post, slug=slug)
    context["post"] = post
    context["comment"] = post.comment.all()
    template_name = "blog/blog_details.html"


    return render(request, template_name, context)




def index(request):

    template_name = "blog/index.html"
    
    return render(request, template_name)


def contact(request):

    template_name = "blog/contact.html"
    
    return render(request, template_name)
