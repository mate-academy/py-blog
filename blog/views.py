from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models, forms


class PostListView(generic.ListView):
    model = models.Post
    queryset = models.Post.objects.select_related("owner")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.filter(id=pk).first()
    if not post:
        return HttpResponseRedirect(reverse("blog:index"))

    if request.method == "POST" and request.user.is_authenticated:
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

    comments = models.Commentary.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "amount_of_comments": len(comments),
        "comment_form": forms.CommentForm(),
    }
    return render(request, "blog/post_detail.html", context=context)
