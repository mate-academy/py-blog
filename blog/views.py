from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.form import CommentaryForm
from blog.models import Post, Commentary, User


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.all().select_related(
        "owner").prefetch_related(
        "comments")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.select_related(
        "owner").prefetch_related(
        "comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.get(request, *args, **kwargs)
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.get_object()
            commentary.save()
            return redirect("blog:post-detail", pk=self.get_object().pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


# def PostDetailView(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             content = request.POST.get("content")
#             Commentary.objects.create(
#                 post=post,
#                 user=request.user,
#                 content=content
#             )
#             return redirect("blog:post-detail", pk=pk)
#         else:
#             return redirect("blog:post-detail", pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})
