from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import User, Commentary, Post


# Create your views here.


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm
    success_url = reverse_lazy("post_detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Commentary.objects.filter(
            post=self.object).order_by(
            "-created_time"
        )
        if "form" not in context:
            context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "You need to login first")
            return self.form_invalid(form)

        comments = form.save(commit=False)
        comments.user = self.request.user
        comments.post = self.object
        comments.save()
        return super().form_valid(form)
