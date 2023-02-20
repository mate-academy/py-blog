from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from blog.forms import AddCommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner"
                                           ).prefetch_related("comments")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class AddCommentView(LoginRequiredMixin, generic.CreateView):
    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = AddCommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
