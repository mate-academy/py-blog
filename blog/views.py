from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from .forms import CommentaryForm

from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    posts = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all().prefetch_related("commentary")


class PostList(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    queryset = Post.objects.all().prefetch_related(
        "commentary__user", "commentary__user__posts"
    )
    paginate_by = 5


class PostDetail(generic.DetailView, FormMixin):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = self.get_form()
        return context

    @login_required
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.user = self.request.user
        comment.save()
        return redirect(self.get_success_url())
