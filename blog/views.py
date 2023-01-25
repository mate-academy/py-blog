from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from blog.models import Post, Commentary
from blog.forms import CommentaryAddForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


def post_detail_and_add_commentary(request, pk):
    post = get_object_or_404(klass=Post, pk=pk)

    if request.method == "POST":
        form = CommentaryAddForm(request.POST)

        if form.is_valid():
            new_comm = Commentary.objects.create(
                user=request.user,
                post=post,
                content=form.cleaned_data["content"]
            )
            new_comm.save()
            url = reverse("blog:post-detail", kwargs={'pk': post.id})
            return HttpResponseRedirect(url)
    else:
        form = CommentaryAddForm()

        return render(
            request,
            "blog/post_detail.html",
            context={"form": form, "post": post}
    )

# def post_detail_and_add_commentary(request, pk):
#     if request.method == "GET":
#         post = Post.objects.get(id=pk)
#         context = {"post": post}
#         return render(request, "blog/post_detail.html", context=context)
#
#     if request.method == "POST":
#         creation_form = CommentaryAddForm(request.POST or None)
#         if creation_form.is_valid():
#             content = request.POST.get("content")
#             comment = Commentary.objects.create(
#                 post=Post.objects.get(id=pk),
#                 user=request.user,
#                 content=content
#             )
#             comment.save()
#             return HttpResponseRedirect(
#                 reverse(
#                     "blog:post-detail", args=[str(pk)]
#                 )
#             )
#
#         else:
#             post = Post.objects.get(id=pk)
#             context = {"error": "Comment should not be empty!", "post": post}
#             return render(request, "blog/post_detail.html", context=context)
