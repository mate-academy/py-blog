from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Prefetch
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.models import Post, Commentary
from blog.forms import CommentaryForm


def index(request: HttpRequest):
    post_list = (
        Post.objects.order_by("-created_time")
        .select_related("owner")
        .annotate(comments_count=Count("comments"))
    )
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related(
        Prefetch(
            "comments",
            queryset=Commentary.objects.select_related("user")
        )
    ).annotate(comment_count=Count("comments"))

    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if not request.user.is_authenticated:
            context = super().get_context_data(form=form)
            context["error"] = "Firstly you have to log in"
            return self.render_to_response(context=context)

        self.object = self.get_object()
        form = CommentaryForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
