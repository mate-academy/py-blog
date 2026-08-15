from django.db.models import Count, QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Post]:
        return (
            Post.objects.select_related("owner")
            .annotate(comment_count=Count("commentaries"))
            .order_by("-created_time")
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self) -> QuerySet[Post]:
        return Post.objects.select_related("owner").prefetch_related(
            "commentaries__user"
        )

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(user=self.request.user)
        return context

    def post(
        self,
        request: HttpRequest,
        *args: object,
        **kwargs: object,
    ) -> HttpResponse:
        self.object = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)
        if not form.is_valid():
            context = self.get_context_data(object=self.object)
            context["form"] = form
            return self.render_to_response(context)

        commentary = form.save(commit=False)
        commentary.user = request.user
        commentary.post = self.object
        commentary.save()
        return redirect(self.object)
