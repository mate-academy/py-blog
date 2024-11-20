from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")


@login_required
def create_comment(request: HttpRequest, pk: int) -> HttpResponse:
    Commentary.objects.create(
        user=request.user,
        post=Post.objects.get(pk=pk),
        content=request.POST.get("text"),
    )
    return redirect("blog:post-detail", pk=pk)
