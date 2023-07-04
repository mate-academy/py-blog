from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from blog.models import Post, Commentary, User
from blog.form import CommentaryForm


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:index")
    template_name = "blog/commentary_form.html"


@login_required
def commentary_create_view(request, pk: int):
    if request.method == "GET":
        context = {
            "form": CommentaryForm(),
            "post_pk": pk,
        }
        return render(request, "blog/commentary_form.html", context)
    elif request.method == "POST":

        user_pk = request.POST["user_pk"]
        post_pk = request.POST["post_pk"]
        content = request.POST["content"]
        form = CommentaryForm(request.POST)

        if form.is_valid():
            Commentary.objects.create(
                user=User.objects.get(pk=user_pk),
                post=Post.objects.get(pk=post_pk),
                content=content,
            )
            return HttpResponseRedirect(reverse("blog:index"))

        context = {
            "form": form
        }
        return render(request, "blog/commentary_form.html", context=context)
