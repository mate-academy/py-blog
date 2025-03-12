from django import forms
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .models import Post, Commentary


def index(request):
    posts_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj
    }

    return render(request, "blog/index.html", context=context)


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['content']


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Commentary.objects.filter(post=post)
        context['comments'] = comments

        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_detail', pk=post.pk)


