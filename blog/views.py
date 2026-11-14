from django.shortcuts import redirect, render
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request):
    post_list = Post.objects.all().order_by("-created_time")[:5]
    return render(request, "blog/index.html", {"post_list": post_list})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentaries"] = Commentary.objects.filter(post=self.object)
        context.setdefault("form", CommentaryForm(user=self.request.user))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(self.get_context_data(form=form))
