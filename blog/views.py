from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post-detail"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["commentaries"] = post.commentaries.all()
        context["owner"] = post.owner.id

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = self.request.user.id
            comment.post_id = self.kwargs.get("pk")
            self.object = comment
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:index")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = "blog/blog_confirm_delete.view"
    success_url = reverse_lazy("blog:index")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    context_object_name = "comment-create"
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:index")

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():

    #         comment = form.save(commit=False)
    #         comment.user_id = self.request.user.id
    #         comment.post_id = self.kwargs.get("pk")

    #         comment.save()
    #         self.object = comment
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return self.form_invalid(form)


class UserView(LoginRequiredMixin, generic.ListView):
    model = User
