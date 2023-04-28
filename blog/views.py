from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CommentaryCreateForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    ordering = ["-created_time"]
    queryset = Post.objects.all().prefetch_related("owner__commentaries")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("owner__commentaries")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    context_object_name = "post-create-comment"

    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = CommentaryCreateForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
