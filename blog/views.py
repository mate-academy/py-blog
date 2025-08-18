from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm()
        comments = post.commentary_set.all().select_related("user")

        context = {
            "post": post,
            "form": form,
            "comments": comments,
        }
        return render(request, self.template_name, context=context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = post
            commentary.save()
            return redirect(request.path)
