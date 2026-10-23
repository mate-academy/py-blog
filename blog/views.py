from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse
from blog.forms import CommentaryForm

from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to post a comment.")
            context = self.get_context_data()
            context["comment_form"] = form
            return self.render_to_response(context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect(
                reverse(
                    "blog:post-detail",
                    kwargs={"pk": self.object.pk}
                )
            )

        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)
