from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Commentary
from .forms import CommentaryModelForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryModelForm()

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryModelForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You are not allowed")
            context = {
                "form": form,
                "post": post,
            }
            return render(request, "blog/post_detail.html",
                          context=context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            return redirect("blog:post-detail", pk=post.id)
        return render(request, "blog/post_detail.html", context={
            "form": form,
            "post": post,
        })
