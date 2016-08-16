from django.shortcuts import render

# Create your views here.

from .forms import PostListForm, QuesForm
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Post
from django.views.generic import ListView
from django.shortcuts import resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/create.html'
    fields = ('title','text','blog','f')


    def form_valid(self, form):
        form.instance.author= self.request.user
        return super(PostCreate, self).form_valid(form)
    def get_success_url(self):
       return resolve_url('questions:detail', pk=self.object.pk)



class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/create.html'
    fields = ('title','text','blog')

    def get_queryset(self):
        return Post.objects.all().filter(author=self.request.user)

    def get_success_url(self):
       return resolve_url('questions:detail', pk=self.object.pk)





class PostView(DetailView):
    model = Post
    template_name = 'post/post.html'

class PostCommentsAjax(DetailView):
    template_name = 'post/post_comments_ajax.html'
    model = Post
    context_object_name = 'post'


class PostList(ListView):
    http_method_names = ["post","get"]
    template_name = 'post/post_list.html'
    model = Post

    def dispatch(self, request, *args, **kwargs):
        self.form = PostListForm(request.GET)
        self.form.is_valid()
        self.qform = QuesForm(request.POST or None)
        return super(PostList, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        queryset = Post.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(title=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[:10]
        queryset = queryset.annotate(answers_count=Count('comments__id'))
        return queryset
    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data(**kwargs)
        context['form'] = self.form
        return context
