from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Commentary
from .forms import CommentaryForm

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.all().select_related("owner").prefetch_related("comments")

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

# Добавьте обработку POST для создания комментария (только для авторизованных)