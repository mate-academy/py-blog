from django.views import generic
from django.shortcuts import redirect

from .models import Post, Commentary
from .forms import CommentaryForm


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentaries"] = (
            self.object.commentaries.order_by("-created_time")
        )

        context.setdefault("form", CommentaryForm())

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.author = request.user
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
