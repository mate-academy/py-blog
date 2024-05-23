from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all().order_by("-created_time")

    for post in all_posts:
        post.num_comments = Commentary.objects.filter(post=post).count()
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "post_list": page_obj.object_list,
    }

    return render(request, "blog/index.html", context=context)


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = "post_list"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context["comments"] = Commentary.objects.filter(
            post=self.object
        ).order_by("-created_time")
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect(
                "login"
            )

        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})
