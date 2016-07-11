from django.views.generic.list import ListView

from django.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post/list.html"
    context_object_name = "posts"
