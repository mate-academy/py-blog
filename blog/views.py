from django.contrib import messages
from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .forms import CommentaryForm
from .models import Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return (
            Post.objects.select_related("owner")
            .annotate(commentaries_count=Count("commentaries"))
            .order_by("-created_time")
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return (
            Post.objects.select_related("owner")
            .prefetch_related("commentaries__user")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = kwargs.get("form") or CommentaryForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            messages.success(request, "Comment added successfully.")
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
