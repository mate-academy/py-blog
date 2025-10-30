from django.contrib import messages
from django.db.models.aggregates import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = (
        Post.objects.annotate(Count("comments"))
        .select_related("author")
        .only("id", "title", "content", "created_time", "author__username")
        .order_by("-created_time")
    )
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    queryset = Post.objects.all().prefetch_related(
        "comments__author", "comments"
    )
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.warning(request, "You are not logged in.")
            return HttpResponseRedirect(reverse_lazy("blog:index"))
        form = self.get_form()
        self.object = self.get_object()
        form.instance.author = self.request.user
        form.instance.post = self.object
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment was successfully posted!")
            return self.form_valid(form)
        messages.warning(request, "Something went wrong.")
        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.id})
