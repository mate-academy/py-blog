from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.form import CommentaryForm

from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    ordering = ("-created_time",)
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_comment"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = post
            commentary.save()
        return self.get(request, *args, **kwargs)
