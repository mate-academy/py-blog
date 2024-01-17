from django.db.models import Count
from django.views import generic

from blog.forms import CommentaryCreationForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryCreationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryCreationForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.save()
        return self.get(request, *args, **kwargs)
