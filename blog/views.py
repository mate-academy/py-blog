from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    )
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    
    def post(self, request, *args, **kwargs) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        content = request.POST.get("content")
        user = request.user
        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)

        comment = Commentary(user=user, post=post, content=content)
        comment.save()

        return redirect(f"/posts/{post.id}/")
