from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = "article_list"

class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'