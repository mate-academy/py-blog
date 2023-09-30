from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


def add_comment(request, pk) -> None:
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get("content")
        if content:
            comment = Commentary(user=request.user, post=post, content=content)
            comment.save()
    return redirect("blog:post-detail", pk=pk)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content")
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
