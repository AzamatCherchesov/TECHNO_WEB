from django.views.generic import DetailView, ListView
from blog.models import Blog


class HomeView(ListView):
    model = Blog
    template_name = 'myproject/home.html'