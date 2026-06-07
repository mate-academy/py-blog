from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from blog.forms import CommentaryForm
from blog.models import Commentary, Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["comments"] = (
            Commentary.objects.filter(post=self.object)
            .select_related("user")
            .order_by("-created_time")
        )
        context.setdefault("form", CommentaryForm())
        return context

    def post(
        self,
        request: HttpRequest,
        *args,
        **kwargs,
    ) -> HttpResponse:
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.is_valid()
            form.add_error(
                None,
                "Only authorized users can post comments.",
            )
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()

            return redirect(
                "blog:post-detail",
                pk=self.object.pk,
            )

        return self.render_to_response(
            self.get_context_data(form=form)
        )
