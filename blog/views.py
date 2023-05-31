from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary
from django.db.models import Count


def index(request):
    post_list = Post.objects.annotate(num_comments=Count("comments"))
    paginator = Paginator(post_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
    }

    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context


class CommentaryCreateView(generic.FormView):
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        post_id = self.kwargs["pk"]
        return reverse_lazy("blog:post-detail", kwargs={"pk": post_id})

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden(
                "You must be logged in to leave a comment."
            )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs["pk"])
        user = self.request.user
        content = form.cleaned_data["content"]
        comment = Commentary.objects.create(
            post=post,
            user=user,
            content=content
        )
        comment.save()
        return super().form_valid(form)
