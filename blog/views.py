from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from .forms import CommentaryForm
from .models import Post, Commentary


# Create your views here
class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.annotate(
        num_comments=Count("commentaries")
    ).order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["commentaries"] = self.object.commentaries.all()
        context["form"] = CommentaryForm(user=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentaryForm(request.POST, user=request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
