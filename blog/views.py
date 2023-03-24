from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic


from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.annotate(commentaries_count=Count("commentaries")).select_related("owner")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries__user")


def commentary_create_view(request, *args, **kwargs):
    if request.method == "POST":
        Commentary.objects.create(
            user_id=request.user.id,
            post_id=kwargs["pk"],
            content=request.POST.get("comment"),
        )

        return redirect("blog:post-detail", pk=kwargs["pk"])

