from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


# def index(request: HttpRequest) -> HttpResponse:
#     posts = Post.objects.order_by("-created_time")
#     paginator = Paginator(posts, 4)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     context = {"posts": posts, "page_obj": page_obj}
#     return render(request, "blog/post_list.html", context)


class Index(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            post = self.get_object()
            form = CommentaryForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return HttpResponseRedirect(
                    reverse("blog:post-detail", kwargs={"pk": post.id})
                )
        return self.get(request, *args, **kwargs)
