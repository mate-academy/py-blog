from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request):
    posts = (Post.objects.all()
             .order_by("-created_time")
             .prefetch_related("comment"))
    is_paginated = 5
    pagination = Paginator(posts, is_paginated)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)

    context = {
        "post_list": page_obj,
        "is_paginated": is_paginated,
        "pagination": pagination,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related(
        Prefetch(
            "comment",
            queryset=Commentary.objects.select_related("user")
        )
    ).select_related("owner")
    form = CommentaryForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.user = request.user
                commentary.post = self.get_object()
                commentary.save()
                return redirect("blog:post-detail", pk=self.get_object().pk)
            else:
                context = self.get_context_data()
                context["form"] = form
                return self.render_to_response(context)
        return self.get(request, *args, **kwargs)
