from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import Blog
from django.views.generic import ListView




class BlogView(DetailView):

    model = Blog
    template_name = 'blog/blog.html'

class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog