from django.shortcuts import redirect, render
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "commentaries__user"
    ).order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        form = CommentaryForm(request.POST)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post_id = request.POST.get("post_id")
            commentary.user = request.user
            commentary.save()
            return redirect("blog:post-detail", kwargs.get("pk"))

        context = {
            "form": form,
            "post": Post.objects.get(id=request.POST.get("post_id"))
        }
        return render(request, "blog/post_detail.html", context=context)
