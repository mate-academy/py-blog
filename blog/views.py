from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary, User


class Index(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        num_commentaries = kwargs["object"].commentaries.count()

        context["num_commentaries"] = num_commentaries

        if self.request.user.is_authenticated:

            context["add_comment_form"] = CommentForm()

        return context


class AddCommentView(generic.UpdateView):

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            user = request.user
            comment = form.save(commit=False)
            comment.user = user
            comment.post = Post.objects.get(id=kwargs["pk"])
            comment.save()

        return redirect(reverse("blog:post-detail", args=[kwargs["pk"]]))
