from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import CommentaryForm
from .models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.user = request.user
            comment.post = post

            comment.save()
        return redirect("blog:post-detail", pk=post.id)


class CommentaryUpdateView(generic.UpdateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.post.pk})

    def get_queryset(self):
        return Commentary.objects.filter(
            user=self.request.user,
        )


class CommentaryDeleteView(generic.DeleteView):
    model = Commentary
    template_name = "blog/commentary_confirm_delete.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.post.pk})

    def get_queryset(self):
        return Commentary.objects.filter(
            user=self.request.user,
        )
