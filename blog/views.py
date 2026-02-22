from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from blog.forms import FormCommentary
from blog.models import Post


class PostsView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"
    queryset = Post.objects.prefetch_related("comments").order_by('-created_time')
    template_name = "blog/index.html"


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = FormCommentary

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form) -> HttpResponse:
        if not self.request.user.is_authenticated:
            form.add_error(None, "You must be logged in")
            return self.form_invalid(form)

        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return super().form_valid(form)
