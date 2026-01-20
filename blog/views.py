from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin, CreateView

from blog.forms import CommentForm
from blog.models import Post, Commentary, User


def index(request):
    posts_list = Post.objects.all().order_by("created_time")
    page = request.GET.get("page", 1)
    paginator = Paginator(posts_list, 5)

    posts = paginator.page(page)

    context = {"post_list": posts}

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Commentary.objects.filter(
            post=self.kwargs["pk"]
        )
        context["count_comments"] = Commentary.objects.filter(
            post=self.kwargs["pk"]
        ).aggregate(count=Count("content"))
        context["form"] = CommentForm()
        return context


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form, *args, **kwargs):
        comment = form.save(commit=False)
        comment.post = Post.objects.get(id=self.kwargs["pk"])
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.kwargs["pk"]})
