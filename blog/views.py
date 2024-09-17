from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ("-created_time",)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.commentaries.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_comment = form.save(commit=False)
            new_comment.post = self.object
            new_comment.owner = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse("blog:index"))
        else:
            messages.error(request, "You have to login or data is not valid")


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "crud/post_form.html"
