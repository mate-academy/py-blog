from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary, User


class IndexListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    @staticmethod
    def post(request: HttpRequest, **kwargs) -> HttpResponse:
        post = Post.objects.get(id=kwargs["pk"])
        form = CommentaryForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                post=post,
                user=request.user,
                **form.cleaned_data
            )
            return redirect("blog:post-detail", pk=kwargs["pk"])

        return render(
            request, "blog/post_detail.html", context={
                "post": post,
                "form": form
            }
        )


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content",)
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")
