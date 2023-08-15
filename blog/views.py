from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import (
    PostSearchForm,
    UserSearchForm,
    IndividualCreationForm,
    CommentarySearchForm,
    CommentaryForm,
)
from blog.models import Post, User, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = PostSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = Post.objects.select_related("owner")
        form = PostSearchForm(self.request.GET)
        if form.is_valid() and "title" in form.cleaned_data:
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")


class UserListView(generic.ListView):
    model = User
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> None:
        context = super(UserListView, self).get_context_data(**kwargs)
        first_name = self.request.GET.get("first_name", "")
        context["search_form"] = UserSearchForm(
            initial={"first_name": first_name}
        )
        return context

    def get_queryset(self) -> None:
        form = UserSearchForm(self.request.GET)
        if form.is_valid():
            queryset = super().get_queryset()
            return queryset.filter(
                first_name__icontains=form.cleaned_data["first_name"]
            )
        return super().get_queryset()


class UserCreateView(generic.CreateView):
    model = User
    form_class = IndividualCreationForm


class CommentaryListView(generic.ListView):
    model = Commentary
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> None:
        context = super(CommentaryListView, self).get_context_data(**kwargs)
        post = self.request.GET.get("post", "")
        context["search_form"] = CommentarySearchForm(initial={"post": post})
        return context

    def get_queryset(self) -> None:
        queryset = Commentary.objects.select_related("user", "post")
        form = CommentarySearchForm(self.request.GET)
        if form.is_valid():
            if "post" in form.cleaned_data:
                return queryset.filter(post__icontains=form.cleaned_data["post"])
        return queryset


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    success_url = reverse_lazy("blog:commentary-list")


class CommentaryDetailView(generic.DetailView):
    model = Commentary
    template_name = "blog/commentary_detail.html"


def add_comment(request, pk) -> None:
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get("content")
        if content:
            comment = Commentary(user=request.user, post=post, content=content)
            comment.save()
    return redirect("blog:post-detail", pk=pk)
