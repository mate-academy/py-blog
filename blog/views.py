from django.shortcuts import redirect, render
from django.views import generic
from django import forms
from django.contrib.sessions.models import Session

from blog.models import Commentary, Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related()


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, pk):
        form = CommentaryForm(request.POST)
        self.object = self.get_object()
        context = self.get_context_data()
        if request.user.is_authenticated and form.is_valid():
            comment = Commentary(
                user=request.user,
                post=self.object,
                content=form.cleaned_data["comment_text"],
            )
            comment.save()
        else:
            context["error"] = "1"
        return self.render_to_response(context)


class CommentaryForm(forms.Form):
    comment_text = forms.CharField(max_length=510)
