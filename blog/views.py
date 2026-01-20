from django.shortcuts import render
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().select_related("owner")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get("pk"))
        user = request.user
        form = CommentaryForm(request.POST)
        context = {
            "post": post,
            "commentary_form": form
        }

        if form.is_valid():
            Commentary.objects.create(
                user=user,
                post=post,
                content=form.cleaned_data["content"]
            )
            context["commentary_form"] = CommentaryForm()
            return render(request, self.template_name, context=context)

        return render(request, self.template_name, context=context)
