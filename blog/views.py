from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django import forms

from blog.models import User, Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ["-created_time"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("owner")
        return queryset


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentaries"] = Commentary.objects.filter(
            post=self.object).select_related("user")
        context["form"] = self.get_comment_form()
        context["error_message"] = self.request.session.pop(
            "error_message", None)
        return context

    def get_comment_form(self):
        return CommentaryForm(self.request.POST or None)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_comment_form()

        if not request.user.is_authenticated:
            request.session["error_message"] = ("You must be logged in to post"
                                                + "a comment.")
            return self.render_to_response(self.get_context_data(form=form))

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect(self.object.get_absolute_url())

        return self.render_to_response(self.get_context_data(form=form))
