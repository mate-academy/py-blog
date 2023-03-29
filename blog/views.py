from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryCreateForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    queryset = Post.objects.select_related("owner")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse_lazy("blog:post-detail", kwargs={"pk": post_id})
        form = CommentaryCreateForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

            return HttpResponseRedirect(post_url)
