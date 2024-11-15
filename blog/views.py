from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import CommentForm


class IndexListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST or None)
    context = {
        "post": post,
        "form": form,
    }

    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return render(request, "blog/post_detail.html", context=context)

    return render(request, "blog/post_detail.html", context=context)
