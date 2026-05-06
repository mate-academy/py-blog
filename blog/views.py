from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse_lazy

from django.views import generic
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView, FormView

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .annotate(num_comments=Count("commentaries"))
        .order_by("-created_time")
    )
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentaries__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentCreateView(FormView):
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Post, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        post_obj = get_object_or_404(Post, pk=self.kwargs["pk"])
        print(form.errors)
        content = form.cleaned_data["content"]
        if not content:
            return redirect("blog:post-detail", pk=self.kwargs["pk"])
        Commentary.objects.create(user=self.request.user,
                                  content=content,
                                  post=post_obj)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]})
