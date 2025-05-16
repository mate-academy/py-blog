from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from blog.models import Post, Commentary


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {
        "post_list": page_obj,        # Змінив з "posts" на "post_list"
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator,
    })


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = CommentaryForm()
        else:
            context['form'] = None
        return context

class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = 'commentary_form.html'  # шаблон не обов’язково використовувати, якщо форму рендериш у post_detail

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_pk = self.kwargs.get('pk')
        form.instance.post = Post.objects.get(pk=post_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})
