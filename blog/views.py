from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse

from .forms import CommentaryForm
from .models import Post


# Create your views here.


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(
            user=self.request.user,
            post=self.object,
        )
        return context

    def post(self, request, *args, **kwargs):
        form = CommentaryForm(
            request.POST,
            user=self.request.user,
            post=self.get_object(),
        )
        if form.is_valid():
            form.save()
        success_url = reverse(
            "blog:post-detail",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        return redirect(success_url)
