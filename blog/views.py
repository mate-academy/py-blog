from django.shortcuts import redirect
from django.views import generic
from blog.models import Post, Commentary
from blog.forms import CommentaryForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    queryset = Post.objects.order_by(
        "-created_time").prefetch_related("commentaries")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentaries"] = Commentary.objects.filter(
            post=self.object).order_by("-created_time")
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.get_object()
            commentary.save()
            return redirect("blog:post-detail", pk=self.get_object().id)
        return self.render_to_response(self.get_context_data(form=form))
