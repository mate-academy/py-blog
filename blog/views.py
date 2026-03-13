from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse
from .forms import CommentaryForm
from django.http import HttpResponseNotAllowed

from blog.models import Post, Commentary
# Create your views here.


class IndexView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])
