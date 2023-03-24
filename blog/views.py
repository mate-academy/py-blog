from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentaryCreateForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post_id = kwargs["pk"]
            post_url = reverse_lazy("blog:post_detail", kwargs={"pk": post_id})
            form = CommentaryCreateForm(request.POST)

            if form.is_valid():
                content = form.cleaned_data["content"]

                if post_id and content:
                    form.instance.user_id = self.request.user.pk
                    form.instance.post_id = post_id
                    self.success_url = post_url
                    return super().form_valid(form)

            return HttpResponseRedirect(post_url)
