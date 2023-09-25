from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries__user")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("content",)

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
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
