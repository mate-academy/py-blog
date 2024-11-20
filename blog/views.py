from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = (
        Post.objects.all()
        .order_by("-created_time")
        .select_related("owner"))


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related("commentaries__user")
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("content",)

    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = CommentaryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
