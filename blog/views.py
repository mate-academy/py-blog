from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").annotate(
        comment_count=Count("commentaries")
    ).order_by("-created_time", "pk")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries__user"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("form", CommentaryForm(user=self.request.user))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.object)
        return self.render_to_response(self.get_context_data(form=form))
