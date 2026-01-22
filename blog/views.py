from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)

    page_number = request.GET.get("page")
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/index.html", {"post_list": posts})


class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.order_by("-created_time")


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("post_comments")
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.post_comments.all()
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return HttpResponseRedirect(
                reverse("login") + "?next=" + request.path
            )
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)
