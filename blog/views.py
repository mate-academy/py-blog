from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from blog.models import Commentary, Post, User


# @login_required
# def index(request):
#
#     post_list = Post.objects.all()
#
#     num_visits = request.session.get("num_visits", 0)
#     request.session["num_visits"] = num_visits + 1
#
#     context = {
#         "post_list": post_list,
#         "num_visits": num_visits + 1,
#     }
#
#     return render(request, "blog/index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    ordering = ["-created_time"]
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")
    template_name = "blog/index.html"
    paginate_by = 5


class UserListView(generic.ListView):
    model = Post
    context_object_name = "user_list"
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post-detail.html"
