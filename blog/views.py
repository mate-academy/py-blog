from django.shortcuts import redirect
from .forms import CommentaryForm
from django.views import generic
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        self.object = self.get_object()
        form = CommentaryForm(self.request.POST, user=self.request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(object=self.object)
        context["comment_form"] = form
        return self.render_to_response(context)
