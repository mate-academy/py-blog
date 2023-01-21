from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    paginate_by = 5
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related(
        "commentaries"
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if "num_visits" in self.request.session:
            self.request.session["num_visits"] += 1
        else:
            self.request.session["num_visits"] = 1
        context["num_visits"] = self.request.session.get("num_visits", 1)
        return context


def post_detail_view(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "GET":
        context = {"post": post, "form": CommentaryForm()}
        return render(request, "blog/post_detail.html", context=context)

    if request.method == "POST":
        form = CommentaryForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get("content")
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=content
            )
            return HttpResponseRedirect(reverse("blog:index"))

        else:
            context = {
                "error": "Comment should not be empty!",
                "post": post,
                "form": form,
            }
            return render(request, "blog/post_detail.html", context=context)
