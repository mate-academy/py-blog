from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import generic

from blog.forms import CreateCommentForm
from blog.models import Post, Commentary


class PostList(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .prefetch_related("commentary_set")
        .order_by("-created_time")
    )


class PostDetailView(generic.DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        context = {
            "post": post,
            "form": CreateCommentForm(),
            "commentary_set": post.commentary_set.all()
        }
        return render(request, "blog/post_detail.html", context=context)

    @staticmethod
    def post(request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        commentary_set = post.commentary_set.all()
        form = CreateCommentForm(request.POST)
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
                    "commentary_set": commentary_set
                }
            )
