from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


# Create your views here.
class IndexListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/index.html"
    context_object_name = "posts"


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "You must be logged in to comment")
            return self.form_invalid(form)

        form.instance.user = self.request.user
        form.instance.post = self.get_object()

        form.save()

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.object.pk}
        )
