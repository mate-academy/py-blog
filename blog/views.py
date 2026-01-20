from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import Post
from .forms import CommentaryForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ["created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.get(request, *args, **kwargs)
