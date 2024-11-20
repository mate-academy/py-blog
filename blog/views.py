from django.views import generic
from django.urls import reverse_lazy

from blog.forms import CommentaryCreateForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["commentary_form"] = CommentaryCreateForm()
        return context
