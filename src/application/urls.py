"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login,logout
from myproject.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rating/', include('like.urls', namespace='rating')),
    url(r'^search/', include('haystack.urls', app_name='search', namespace='search')),
    url(r'^news/', include('post.urls', namespace="questions")),
    url(r'^blogs/', include('blog.urls', namespace="blogs")),
    url(r'^login/$', login,{'template_name': 'myproject/login.html'}, name="login"),
    url(r'^logout/$', logout,{"next_page":"blogs:blog_list"}, name="logout"),
    url(r'^$', HomeView.as_view(), name="homelist"),

]


