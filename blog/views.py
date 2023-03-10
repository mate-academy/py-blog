from django.shortcuts import render, redirect
from django.views import generic
from .forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related(
        "commentaries"
    ).order_by("created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    context_object_name = "post_detail"
    model = Post
    queryset = Post.objects.prefetch_related(
        "commentaries"
    ).select_related(
        "owner"
    ).order_by("created_time")

    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():

            Commentary.objects.create(
                **form.cleaned_data,
                post_id=self.object.pk,
                user_id=self.request.user.id
            )
            return redirect("blog:post-detail", pk=self.object.pk)
        else:
            return render(request, "blog:post_list")
