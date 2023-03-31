from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Commentary, User
from .forms import PostSearchForm, UserCreationForm


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("owner")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PostListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = PostSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Post.objects.select_related("owner")
        form = PostSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )

        return queryset


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form) -> HttpResponse:
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(id=self.kwargs["pk"])
        comment.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("blog:index")
