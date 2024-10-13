from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    )
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_object(self, queryset=None) -> Post:
        return Post.objects.prefetch_related("commentaries__user").get(
            id=self.kwargs["pk"]
        )

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm

        return context

    def post(self, request, **kwargs) -> HttpResponse:
        form = CommentaryForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.post = post
            form.save()
            return HttpResponseRedirect(
                reverse("blog:post-detail", kwargs={"pk": post.id})
            )
        return render(
            request, "blog/post_detail.html", context={
                "post": post, "form": form
            }
        )
