from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by(
        "-created_time"
    ).select_related("owner").prefetch_related("commentaries")
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentaries__user")
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.user = self.request.user
            obj.save()
            return redirect("blog:post-detail", post.pk)


class CommentaryCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView
):
    model = Commentary
    form_class = CommentForm
    success_message = "Comment was created successfully"

    def get_context_data(self, **kwargs):
        context = super(CommentaryCreateView, self).get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super(CommentaryCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"], })
