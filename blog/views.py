import datetime
from django.views import generic

from blog.models import Post, Commentary
from blog.forms import CommentaryForm


class PostView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Commentary.objects.filter(
            post=self.get_object()).order_by("-created_time")
        data["commentaries"] = comments_connected
        if self.request.user.is_authenticated:
            data["comment_form"] = CommentaryForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Commentary(
            content=request.POST.get("content"),
            user=self.request.user,
            post=self.get_object(),
            created_time=datetime.datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%SZ"))
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
