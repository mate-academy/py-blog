from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, edit

from .models import Post, Commentary, User
from .forms import CommentForm


def index(request: HttpRequest) -> HttpResponse:
    return redirect("blog:post-list")


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comments").select_related()
    paginate_by = 5


class PostDetailView(edit.FormMixin, DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comments").select_related()
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def post(self, request: HttpRequest, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if not form.is_valid() or not request.user.id:
            return self.form_invalid(form)
        user = User.objects.get(id=request.user.id)
        post = Post.objects.get(id=self.object.id)
        content = form.cleaned_data["content"]
        Commentary.objects.create(user=user, post=post, content=content)
        return HttpResponseRedirect(self.get_success_url())
