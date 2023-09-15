from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.form import CommentForm
from blog.models import Commentary

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    context_object_name = "post_list"


class PostDetailView(generic.DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm()
        commentaries = post.commentaries.all()
        context = {
            "post": post,
            "form": form,
            "commentaries": commentaries
        }
        return render(request, "blog/post_detail.html", context=context)

    @staticmethod
    def post(request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        commentaries = post.commentaries.all()
        form = CommentForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post=post,
                content=form["content"].data
            )
            return render(
                request,
                "blog/post_detail.html",
                context={
                    "post": post,
                    "form": form,
                    "commentaries": commentaries
                }
            )
