from django.views import generic
from django.views.generic.edit import FormMixin
from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm
