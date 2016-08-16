from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import Article


class NewsView(DetailView):

    model = Article
    template_name = 'article.html'
    context_object_name = 'article'


def show_news(request, news_id=0, cat_id=0):
    return render(request, 'blabla.html', {"news_id": news_id})
