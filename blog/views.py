from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:index")
