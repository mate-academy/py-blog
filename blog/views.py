from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


def commentary_create_view(request: HttpRequest, pk: int):
    user = request.user
    if user.is_anonymous:
        return ValidationError("Log in to comment.")
    content = request.POST["content"]
    Commentary.objects.create(user=user, content=content, post_id=pk)
    return HttpResponseRedirect(reverse("blog:post-detail", kwargs={"pk": pk}))
