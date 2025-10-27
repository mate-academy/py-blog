from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.models import Post
from blog.forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm
    queryset = Post.objects.prefetch_related("commentaries__user")

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if "form" not in context:
            context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = self.request.user
        comment.save()

        return super().form_valid(form)
