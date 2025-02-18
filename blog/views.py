from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments__user")
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        context["comments"] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(
            self.get_context_data(commentary_form=form)
        )
