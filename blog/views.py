from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        post_object = self.get_object()
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post_object
                comment.save()
        return super().get(request, *args, **kwargs)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
