from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")


class PostDetailView(FormMixin, generic.DetailView):
    queryset = Post.objects.prefetch_related("commentaries")
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form: CommentaryForm) -> HttpResponse:
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid() and request.user.is_authenticated:
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self) -> str:
        return self.request.path
