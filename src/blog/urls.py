
from django.conf.urls import url
from django.contrib import admin
from .views import BlogView, BlogList


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^blogs/$', BlogList.as_view(), name="blog_list"),



    #url(r'^(?P<news_id>\d+)/$', 'news.views.show_news'),
    #url(r'^(?P<news_id>\d+)/like/$', 'news.views.show_news'),
]



