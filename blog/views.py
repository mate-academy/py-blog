from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from blog.form import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = "-created_time"
    queryset = Post.objects.select_related("owner")
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(comment_count=Count("commentaries"))
        return queryset


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm


class CreateCommentaryView(LoginRequiredMixin, generic.CreateView):

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
