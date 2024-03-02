from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexListView(generic.ListView):
    queryset = Post.objects.select_related("owner")
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(
            initial={"post": self.object, "user": self.request.user}
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content")
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META["HTTP_REFERER"]
        return context


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ("title", "content")
    success_url = reverse_lazy("blog:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META["HTTP_REFERER"]
        return context


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META["HTTP_REFERER"]
        return context


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(owner_id=self.request.user.id)
        context["previous_url"] = self.request.META["HTTP_REFERER"]
        return context
