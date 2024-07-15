from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


@login_required
def create_comment_view(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                post_id=pk, user=request.user, **form.cleaned_data
            )
    return HttpResponseRedirect(reverse("blog:post-detail", args=(pk,)))
