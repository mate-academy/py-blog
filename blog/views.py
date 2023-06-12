from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner")
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs["pk"])
        user = request.user
        form = CommentaryForm(request.POST)
        context = {"post": post, "commentary_form": form}

        if form.is_valid():
            Commentary.objects.create(
                user=user,
                post=post,
                content=form.cleaned_data["content"]
            )
            context["commentary_form"] = CommentaryForm()
            return render(request, "blog/post_detail.html", context=context)

        return render(request, "blog/post_detail.html", context=context)
