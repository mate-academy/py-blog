from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .forms import PostForm, EditForm, CommentaryCreateForm
from .models import Post, Commentary


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments")

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["commentary_form"] = CommentaryCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        content = request.POST.get("content")
        pk = kwargs.get("pk")
        Commentary.objects.create(
            user=request.user,
            post_id=pk,
            content=content
        )
        return redirect("blog:post-detail", pk)


class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_add.html"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/post_update.html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:index")
