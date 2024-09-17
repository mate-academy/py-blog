from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        commentaries = post.commentaries.all()
        form = CommentaryForm()
        return render(request,
                      "blog/post_detail.html",
                      {
                          "post": post,
                          "commentaries": commentaries,
                          "form": form
                      })

    @staticmethod
    def post(request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        commentaries = post.commentaries.all()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = Commentary(
                user=request.user,
                post=post,
                content=form["content"].data
            )
            commentary.save()
        return render(request, "blog/post_detail.html", {
            "post": post,
            "commentaries": commentaries,
            "form": form
        })


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
