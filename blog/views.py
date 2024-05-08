from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.models import Post, Commentary
from .forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ("-created_time", )
    template_name = "blog/index.html"
    queryset = Post.objects.annotate(comment_count=Count("commentary"))


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        commentary = form.save(commit=False)
        commentary.user = self.request.user
        commentary.post = self.object
        commentary.save()
        return super().form_valid(form)


# def comment_create(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.user = request.user
#                 comment.post = self.o
#                 comment.save()
#                 return redirect("blog:post-detail", pk=post_id)
#         else:
#             messages.error(request, "You must be logged in to leave a comment.")
#     else:
#         form = CommentForm()
#
#     return render(request, "blog/comment_form.html", {"form": form})
