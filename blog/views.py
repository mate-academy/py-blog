from django.contrib.auth import get_user_model, login
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CustomUserCreationForm, CommentaryForm, PostForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related("commentary_set")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.select_related("owner").prefetch_related("commentary_set__user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.get_object()
        comment_list = post.commentary_set.all()
        paginator = Paginator(comment_list, 3)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["paginator"] = paginator
        context["is_paginated"] = True
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(generic.CreateView):
    form_class = CommentaryForm
    model = Commentary
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user_id = self.request.user.id
            commentary.post_id = self.kwargs["pk"]
            commentary.save()

        return redirect('blog:post-detail', pk=self.kwargs['pk'])


class PostCreateView(generic.CreateView):
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner_id = self.request.user.id
            post.save()

        return redirect('blog:index')


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    model = get_user_model()
    template_name = "registration/sign_up.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("blog:index")
