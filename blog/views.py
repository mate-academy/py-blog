from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:post-detail")

    def post(self, request, *args, **kwargs):
        Commentary.objects.create(
            user=request.user,
            content=request.POST["content"],
            post=Post.objects.get(title=request.POST["post"])
        )
        return redirect(request.META.get("HTTP_REFERER"))
