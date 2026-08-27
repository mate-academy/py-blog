from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return (
            Post.objects
            .prefetch_related("comments__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "Login required")
            return self.get(request, *args, **kwargs)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(request.path)

        return self.get(request, *args, **kwargs)
