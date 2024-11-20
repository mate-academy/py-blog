from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from blog.models import Post
from blog.forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/blog_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    slug_field = "slug"

    form = CommentaryForm

    def post(self, request, *args, **kwargs):
        form = CommentaryForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("blog:post-detail", kwargs={
                "pk": post.pk
            }))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context
