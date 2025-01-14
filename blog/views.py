from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (Post.objects.order_by("-created_time").
                select_related("owner").prefetch_related("comments"))
    paginate_by = 5


class PostDetailView(generic.DetailView, generic.CreateView):
    model = Post
    fields = []
    template_name = "blog/post_detail.html"
    queryset = (Post.objects.all().select_related("owner").
                prefetch_related("comments__user"))

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.get_object().pk}
        )

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment = request.POST.get("content").strip()
        if comment:
            Commentary.objects.create(
                content=comment,
                post=post,
                user=request.user,
            )
        return HttpResponseRedirect(self.get_success_url())
