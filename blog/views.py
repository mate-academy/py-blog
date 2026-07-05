from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        return (queryset.select_related("owner")
                .prefetch_related("commentaries"))

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentaries.all()
        context["form"] = CommentaryForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()

        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must login to the website")
        elif form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()

            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)


class UserDetailView(DetailView):
    model = get_user_model()
    context_object_name = "user_profile"
