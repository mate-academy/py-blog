from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    paginate_by = 5
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentary_set"))


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentary_set__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentary_form'] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm

    def form_valid(self, form):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs.get("post_id")
        return redirect("blog:post-detail", pk=post_id)