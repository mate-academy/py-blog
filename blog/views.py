from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(
                reverse("blog:post-detail", kwargs={"pk": post.id})
            )

        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)
