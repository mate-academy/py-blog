from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


# @login_required
# def index(request):
#     post_list = Post.objects.all().order_by("-created_at")
#
#     context = {
#         "post_list": post_list
#     }
#
#     return render(request, "blog/index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("/")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:post-detail")

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(id=self.request.GET["pk"])
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.request.GET["pk"]})
