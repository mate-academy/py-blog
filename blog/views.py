from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by("-created_time") # noqa


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm
        return context

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST,
                              user=request.user,
                              post=self.object)

        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
