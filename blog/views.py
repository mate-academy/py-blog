from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = (Post.objects.
             select_related("owner").
             prefetch_related("comments").
             all())
    paginator = Paginator(posts, 5)

    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)
    context = {
        "post_list": post_list,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.get_object().id)
        context = self.get_context_data(object=self.get_object(), form=form)
        return self.render_to_response(context)
