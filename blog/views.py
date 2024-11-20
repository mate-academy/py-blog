from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import ListView, DetailView
from blog.models import Post, Commentary
from django.views.generic.edit import FormMixin
from blog.forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.prefetch_related(
        "comments"
    ).order_by("-created_time")
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(FormMixin, DetailView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "comments"
    ).order_by("-created_time")
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={
            "pk": self.object.id
        })

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                content=request.POST["content"],
                post_id=kwargs["pk"]
            )
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)
