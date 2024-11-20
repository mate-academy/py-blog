from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.order_by("-created_time")
    num_posts = post_list.count()

    paginator = Paginator(post_list, 5)
    page = request.GET.get("page", 1)
    page_obj = paginator.get_page(page)

    context = {
        "post_list": page_obj,
        "num_posts": num_posts,
        "page_obj": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        else:
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
