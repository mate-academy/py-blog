from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    queryset = Post.objects.select_related("owner")
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context["comments"] = Commentary.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = self.request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)

        context = self.get_context_data(object=post)
        context["form"] = form
        return self.render_to_response(context)
