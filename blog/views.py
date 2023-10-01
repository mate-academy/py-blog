from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, FormView

from .models import Post, Commentary
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ["-created_time"]
    template_name = "blog/index.html"


class PostDisplayView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDisplayView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryFormView(SingleObjectMixin, FormView):
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm
    model = Commentary

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs["pk"])

        if not request.user.is_authenticated:
            form = self.get_form()
            form.add_error(
                "content",
                "You must be logged in to leave a comment."
            )
            context = {"form": form, "post": post}
            return render(request, "blog/post_detail.html", context=context)

        self.object = Commentary(
            user=request.user, post=post, content=request.POST["content"]
        )
        self.object.save()

        return HttpResponseRedirect(
            reverse("blog:post-detail", kwargs={"pk": kwargs["pk"]})
        )


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentaryFormView.as_view()
        return view(request, *args, **kwargs)
