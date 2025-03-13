from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class Index(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post = self.get_object()
            form = CommentaryForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return HttpResponseRedirect(
                    reverse("blog:post-detail", kwargs={"pk": post.id})
                )
        return self.get(request, *args, **kwargs)
