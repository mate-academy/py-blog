from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.annotate(num_commentaries=Count(
        "commentaries")).order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(View):
    @staticmethod
    def post(request: HttpRequest, pk: int) -> HttpResponse:
        post = get_object_or_404(Post, id=pk)
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.save()
            return redirect("blog/post-detail", pk=pk)
        return render(request, "blog/post-detail",
                      {"form": form})
