from django.views import generic
from django.views.generic import DetailView
from django.shortcuts import redirect
from django import forms
from django.db import models
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").annotate(
        comments_count=models.Count("commentaries"),
    )
    context_object_name = "post_list"


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write your comment here..."}
            )
        }
        labels = {"content": ""}


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(form=CommentaryForm(), **kwargs)

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect("blog:post-detail", pk=post.pk)
