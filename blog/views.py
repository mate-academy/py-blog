from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/comment_form.html"


class PostDetailView(generic.DetailView):
    model = Post


@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logged_out.html")
