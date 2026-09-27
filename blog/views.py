from django.contrib import messages
from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        """Fetch posts with owners and commentary counts in a single
        query to avoid N+1 lookups while rendering the feed. Ordering
        is set explicitly: grouping (annotation) would otherwise ignore
        the model's default Meta ordering."""
        return (
            Post.objects
            .select_related("owner")
            .annotate(commentaries_count=Count("commentaries"))
            .order_by("-created_time")
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.select_related("owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_list"] = (
            self.object.commentaries.select_related("user")
        )
        if "form" not in context:
            context["form"] = CommentaryForm(request_user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST, request_user=request.user)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()
            messages.success(request, "Your commentary has been added.")
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
