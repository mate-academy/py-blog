from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5
    ordering = "-created_time"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = CommentaryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
