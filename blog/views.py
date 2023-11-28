from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from services.post_services import get_posts
from .form import CommentaryForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    queryset = get_posts()
    paginate_by = 5


class PostDetailView(
    FormMixin,
    generic.DetailView,
):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = get_posts(comments=True)
    form_class = CommentaryForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.get_object().id})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
