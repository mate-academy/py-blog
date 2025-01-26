from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models.aggregates import Count
from django.urls import reverse, reverse_lazy
from django.views import generic

from blog.models import Post, Commentary
from blog.forms import CommentaryForm



class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").annotate(com_num=Count("comments"))
    template_name = "base.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset =  Post.objects.select_related("owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["com_form"] = CommentaryForm()
        return context


@login_required
def create_comment_view(request, pk: int):
    post_obj = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = Commentary()
            commentary.post = post_obj
            commentary.user = request.user
            commentary.content = form.cleaned_data["comment"]
            commentary.save()
            return redirect("blog:post-detail", pk=pk)
    else:
        form = CommentaryForm()
        return render(request, "blog/post_detail.html", {"post": post_obj, "com_form": form })
