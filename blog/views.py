from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = (Post.objects.all().
                select_related("owner").
                prefetch_related("commentaries").
                order_by("-created_time"))
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.all().select_related("owner").
                prefetch_related("commentaries__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = CommentaryForm()

        return context


class CommentCreateView(generic.CreateView):
    model = Commentary
    form_class = CommentaryForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(
                None,
                "Only authorized users can post comments."
            )
            return self.form_invalid(form)

        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]

        return super().form_valid(form)

    def form_invalid(self, form):
        post = get_object_or_404(
            Post.objects
            .select_related("owner")
            .prefetch_related("commentaries__user"),
            pk=self.kwargs["pk"],
        )

        return render(
            self.request,
            "blog/post_detail.html",
            {
                "post": post,
                "form": form,
            },
        )

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]},
        )
