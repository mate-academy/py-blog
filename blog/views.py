from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from blog.forms import CommentaryForm
from blog.models import Post


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("index")

    form = AuthenticationForm(
        request, data=request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("index")

    return render(request, "login", {"form": form})


class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .annotate(
            comments_count=Count("commentaries")
        ).order_by("-created_time")
    )


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["commentaries"] = post.commentaries.select_related(
            "user"
        ).order_by("-created_time")
        context["post"] = post
        context.setdefault("form", CommentaryForm())
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.user = request.user
            comment.save()
            return redirect(self.template_name)

        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
