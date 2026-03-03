from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request):
    """View function for the home page of the site."""

    num_posts = Post.objects.order_by("-created_time")
    paginator = Paginator(num_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "page_obj": page_obj,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated():
            new_comment = Commentary(
                user=request.user,
                post=self.object,
                content=request.POST.get("comment", ""),
            )
            new_comment.save()
        return redirect("blog:post-detail", pk=self.object.pk)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context
