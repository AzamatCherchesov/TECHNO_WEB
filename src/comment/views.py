from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, resolve_url

# Create your views here.
from django.views.generic import CreateView
from models import Comment
from post.models import Post


class PostComment(LoginRequiredMixin, CreateView):
    template_name = 'comment/comment.html'
    model = Comment
    fields = ('text',)

    # author post
    def dispatch(self, request, pk=None, *args, **kwargs):
        self.ppk = Post.objects.get(pk=pk)
        return super(PostComment, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostComment, self).get_context_data(**kwargs)
        context['pk'] = self.ppk
        return context

    def form_valid(self, form):
        # Saving valid form
        form.instance.author = self.request.user
        form.instance.post = self.ppk
        return super(PostComment, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("questions:detail", pk=self.ppk.pk)
