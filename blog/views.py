from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse
from django.views import generic

from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().select_related("owner")
    template_name = "blog/index.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(num_comments=Count("commentary"))
        return queryset


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_pk = self.kwargs.get("post_pk")
        if post_pk:
            form.instance.post = Post.objects.get(pk=post_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail", args=[self.kwargs["post_pk"]])
