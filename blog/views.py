from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, FormView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.select_related("owner").prefetch_related("commentaries")
    )
    ordering = "-created_time"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context
    # form_class = CommentaryForm

    # def get_success_url(self):
    #     return reverse("blog:post-detail", kwargs={"pk": self.object.pk})
    #
    # def get_context_data(self, **kwargs):
    #     context = super(PostDetailView, self).get_context_data(**kwargs)
    #     context["form"] = self.get_form()
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden()
    #     form = self.get_form()
    #     self.object = self.get_object()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     return self.form_invalid(form)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.post = Post.objects.get(pk=self.object.pk)
    #     return super(PostDetailView, self).form_valid(form)


class CommentaryFormView(generic.FormView, SingleObjectMixin):
    form_class = CommentaryForm
    model = Commentary
    template_name = "blog/commentary_form.html"
    success_url = "#"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class PostCommentView(generic.View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentaryFormView.as_view()
        form = CommentaryForm(request.POST)
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/accounts/login/")
        form.instance.user = request.user
        form.instance.post = Post.objects.get(id=self.kwargs["pk"])
        if form.is_valid():
            form.save()
        return view(request, *args, **kwargs)
