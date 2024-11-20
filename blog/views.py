from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, User, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_object()
        comments = Commentary.objects.filter(post=posts)
        context["comments"] = comments
        context["comment_form"] = CommentaryForm()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        content = request.POST.get("content")
        pk = kwargs.get("pk")
        Commentary.objects.create(user=request.user,
                                  post_id=pk,
                                  content=content)
        return redirect("blog:post-detail", pk)


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
