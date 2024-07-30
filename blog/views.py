from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary, User


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")
    context = {"posts": post_list}
    return render(
        request,
        "blog/index.html",
        context=context
    )


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = (
        Post.objects.select_related("owner").prefetch_related("commentary")
    )


class PostDetailView(DetailView):
    model = Post
    queryset = (
        Post.objects.select_related("owner").prefetch_related("commentary")
    )
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = Commentary.objects.filter(post=post)
        if self.request.method == 'POST':
            content = self.request.POST.get('content')
            if content:
                Commentary.objects.create(
                    post=post,
                    owner=self.request.user,
                    content=content
                )
                return redirect(self.get_object().get_absolute_url())
        return context


class CommentaryCreateView(CreateView):
    model = Commentary
    fields = ['content']
    template_name = 'blog/commentary_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'blog:post-detail', kwargs={'pk': self.kwargs['pk']}
        )


class CommentaryListView(ListView):
    model = Commentary


class UserDetailView(DetailView):
    model = User
    template_name = "blog/user_detail.html"
    context_object_name = "user"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    success_url = reverse_lazy("blog:user-detail")
    template_name = "blog/user_form.html"

    def get_success_url(self):
        return reverse('blog:user-detail', kwargs={'pk': self.object.pk})

