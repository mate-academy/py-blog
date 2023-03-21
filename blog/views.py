from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Commentary, User
from .forms import PostSearchForm, CommentaryForm, UserCreationForm


class PostListView(LoginRequiredMixin, generic.ListView):
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

    # def get_queryset(self) -> QuerySet:
    #     queryset = Post.objects.select_related("owner")
    #     form = PostSearchForm(self.request.GET)
    #     if form.is_valid():
    #         return queryset.filter(
    #             title__icontains=form.cleaned_data["title"]
    #         )
    #
    #     return queryset


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    success_url = reverse_lazy("blog:index")


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("blog:index")
