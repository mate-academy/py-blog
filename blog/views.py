from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")
    form_class = CommentaryForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form: CommentaryForm) -> HttpResponse:
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.get_form()

        if form.is_valid() and request.user.is_authenticated:
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self) -> str:
        return self.request.path
