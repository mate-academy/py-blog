from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.models import Post, Commentary, User
from blog.forms import CommentaryForm


def index(request):
    post_list = Post.objects.order_by("-created_time")

    # info about blog
    num_users = User.objects.count()
    num_posts = Post.objects.count()

    if "page" in request.GET:
        page = request.GET["page"]
    else:
        page = 1
    paginator = Paginator(post_list, 5)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {
        "post_list": post_list,
        "num_users": num_users,
        "num_posts": num_posts,
        "page": page
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={
            "pk": self.object.id
        })

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                content=request.POST["content"],
                post_id=kwargs["pk"]
            )
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)
