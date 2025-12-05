from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django import forms
from .models import Post, Commentary


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class CommentaryForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 4,
                "class": "form-control",
                "placeholder": "Escreva seu comentário aqui..."
            })
        }



class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.object.get_absolute_url())

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
