from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.order_by("-created_time")

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
    }
    return render(request, "blog/post_list.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.content = request.POST["content"]
            comment.save()
            return HttpResponseRedirect(self.request.path)

        return redirect("login")
