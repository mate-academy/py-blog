from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from .forms import CommentForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.annotate(
        comments_count=Count("post_comments")
    ).order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "post_comments__user"
    ).annotate(
        comments_count=Count("post_comments")
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm(request=self.request)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST, request=request)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        else:
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)
