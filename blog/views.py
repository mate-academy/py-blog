from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from blog.forms import CommentForm
from blog.models import Post


def index(request):
    posts = (
        Post.objects.all()
        .annotate(comments_count=Count("comments"))
        .order_by("-created_time")
    )

    paginator = Paginator(posts, 5)  # по 5 постів на сторінку
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "post_list": page_obj,  # ⚡ ТЕПЕР posts = поточна сторінка постів
        "page_obj": page_obj,
        "is_paginated": paginator.num_pages > 1,
        "paginator": paginator,
    }

    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        # усі коментарі до поста
        context["comments"] = post.comments.all().order_by("-created_time")

        # порожня форма для нового коментаря
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """Обробляє створення нового коментаря."""
        self.object = self.get_object()
        if not request.owner.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.author
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        # якщо форма невалідна — показуємо з помилками
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
