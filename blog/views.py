from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from blog.models import Post, User
from blog.forms import CommentForm


class PostDetailView(DetailView):
    model = Post
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))


class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = (Post.objects.select_related("owner").
                prefetch_related("commentaries"))
    template_name = "blog/index.html"

    num_users = User.objects.count()
    num_posts = Post.objects.count()
    extra_context = {"num_users": num_users, "num_posts": num_posts}
