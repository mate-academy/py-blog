from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.all().order_by("-created_time").select_related(
        "owner"
    ).prefetch_related("commentaries")
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        context = {}
        form = CommentaryForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                commentary = form.save(commit=False)
                commentary.user = request.user
                commentary.post = self.object
                commentary.save()

                return redirect(
                    reverse(
                        "blog:post-detail", kwargs={"pk": self.object.pk}
                    )
                )
            else:
                context["error"] = "You must be logged in to post a comment"

        return self.render_to_response(
            self.get_context_data(commentary_form=form, **context)
        )
