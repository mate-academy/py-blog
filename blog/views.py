from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)
    context = {
        "post_list": post_list,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = self.get_object()
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.post = post
            instance.save()
            return HttpResponseRedirect(reverse("blog:post-detail", args=[instance.post.id]))
        return render(request, "blog/post_detail.html", {"form": form, "pk": post.id, "post" : post} )

