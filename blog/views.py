from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentaries")
    paginate_by = 5


def post_detail_view(request, pk):
    if request.method == "GET":
        context = {
            "form": CommentaryForm(),
            "post": Post.objects.get(pk=pk)
        }
        return render(request, "blog/post_detail.html", context=context)

    elif request.method == "POST":
        user_id = request.session.get("_auth_user_id")
        form = CommentaryForm(request.POST)

        if form.is_valid() and user_id:
            Commentary.objects.create(
                user_id=user_id,
                post_id=pk,
                **form.cleaned_data
            )
            return HttpResponseRedirect(reverse(
                "blog:post-detail",
                kwargs={"pk": pk}
            ))

        login_error = "Only authorized users can post comments."

        context = {
            "form": form,
            "post": Post.objects.get(pk=pk),
            "login_error": login_error if not user_id else None
        }

        return render(request, "blog/post_detail.html", context=context)
