from blog.forms import CommentForm
from blog.models import Post, Commentary
from django.shortcuts import render, redirect
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentary_set")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "commentary_set").select_related("owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            Commentary.objects.create(
                **form.cleaned_data,
                post_id=self.object.pk,
                user_id=self.request.user.id
            )
            return redirect("blog:post-detail", pk=self.object.pk)
        else:
            return render(request, "")
