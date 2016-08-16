
from django.conf.urls import url
from django.contrib import admin
from comment.views import PostComment
from .views import PostView, PostList, PostCreate, PostEdit, PostCommentsAjax

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^create/$', PostCreate.as_view(), name="post_create"),
    url(r'^(?P<pk>\d+)/edit/$', PostEdit.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/ajax/$', PostCommentsAjax.as_view(), name="post_comments"),
    url(r'^(?P<pk>\d+)/comment/$', PostComment.as_view(), name="post_comment"),
    #url(r'^(?P<news_id>\d+)/$', 'news.views.show_news'),
    #url(r'^(?P<news_id>\d+)/like/$', 'news.views.show_news'),
]


