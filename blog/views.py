from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, CreateView, ListView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator


def index_view(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    context = {"post_list": posts}
    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(CreateView):
    model = Commentary
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super(CommentaryCreateView, self).get_context_data(**kwargs)
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        context["post"] = post
        context["user"] = self.request.user
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            post_id = self.kwargs.get("post_id")
            post = get_object_or_404(Post, pk=post_id)
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post_id)
