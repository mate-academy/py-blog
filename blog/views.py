from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Post, Commentary
from blog.forms import CommentaryForm


def index(request):
    all_posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "all_posts": all_posts,
        "page_obj": page_obj,
        "post_list": page_obj.object_list,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    queryset = Post.objects.prefetch_related(
        Prefetch(
            "commentary",
            queryset=Commentary.objects.select_related("user")
        )
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Commentary
    fields = ["content"]
    template_name = "blog/comment_form.html"
    success_url = reverse_lazy("blog:post_detail")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
