from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    queryset = Post.objects.all().prefetch_related("owner__commentaries")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    queryset = Post.objects.all().prefetch_related("owner__commentaries")

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # if self.request.user.is_authenticated:
        context["form"] = self.form_class()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    queryset = Commentary.objects.all().prefetch_related("user__posts")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            comment = form.save(commit=False)
            comment.user = user
            comment.post = Post.objects.get(id=kwargs["pk"])
            comment.save()
        return redirect(reverse("blog:post-detail", args=[kwargs["pk"]]))

    def get(self, request, *args, **kwargs):
        return redirect(reverse("blog:post-detail", args=[kwargs["pk"]]))
