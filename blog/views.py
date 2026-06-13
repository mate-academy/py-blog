from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from blog.forms import CommentaryForm
from blog.models import Post


def index(request):
    posts = Post.objects.annotate(
        comment_count=Count("commentaries")).order_by(
        "-created_time"
    )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "post_list": page_obj}
    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return Post.objects.prefetch_related("commentaries__user")

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if not request.user.is_authenticated:
            form.add_error(None, "Only authorizated users can leave a comment")
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.post = self.object
            comment.save()
        return redirect("blog:post-detail", pk=self.object.pk)
