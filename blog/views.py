from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentaryForm
from django.views.generic.edit import FormMixin


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'
    queryset = Post.objects.select_related('owner').prefetch_related('commentaries')
    paginate_by = 5


class PostDetailView(FormMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm
    queryset = Post.objects.select_related("owner").prefetch_related("commentaries__user")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        self.success_url = reverse_lazy("blog:post-detail", kwargs={ "pk": self.get_object().id })

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.user = self.request.user

        comment.save()
        return super().form_valid(form)
