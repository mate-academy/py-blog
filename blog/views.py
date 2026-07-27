from django import forms
from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from blog.models import Commentary, Post


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not (self.user and self.user.is_authenticated):
            raise forms.ValidationError(
                "You must be logged in to leave a comment."
            )
        return cleaned_data


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").annotate(
        comments_count=Count("commentaries")
    ).order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries__user"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("comment_form", CommentaryForm())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)
