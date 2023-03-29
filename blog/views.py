from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.order_by("created_time")
    template_name = "blog/index.html"


class PostDetailViewWithComment(generic.DetailView, generic.CreateView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )

    def form_valid(self, form):
        form.instance.post = Post.objects.get(
            pk=self.kwargs["pk"]
        )
        form.instance.user = self.request.user
        form.instance.created_time = (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return super().form_valid(form)
