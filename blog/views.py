from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from .models import (Post,
                     Commentary,
                     CustomUser)
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context["comments"] = Commentary.objects.filter(
            post=self.object
        ).order_by("-created_time")
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return redirect(
                reverse(
                    "blog:post-detail",
                    kwargs={
                        "pk": self.object.pk
                    }
                )
            )
        return self.render_to_response(
            self.get_context_data(form=form)
        )


class CustomUserListView(generic.ListView):
    model = CustomUser
    paginate_by = 5


class CustomUserDetailView(generic.DetailView):
    model = CustomUser
    template_name = "blog/user_detail.html"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.object.post.pk})
