from django.views import generic

from .models import Post
from .forms import CommentaryForm


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = (self.object.commentary_set.all()
                               .order_by("-created_time"))

        context["form"] = CommentaryForm()

        return context
