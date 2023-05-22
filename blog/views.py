from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import UserCreateForm
from .models import Post, User, Commentary


class Index(generic.ListView):
    """View function for home page of site."""

    model = Post
    queryset = Post.objects.all().select_related("owner")
    num_posts = Post.objects.all().count()
    num_users = User.objects.count()
    template_name = "blog/index.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_posts"] = Post.objects.all().count()
        context["num_users"] = User.objects.count()
        return context


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.owner = self.request.user
        return super().form_valid(form)


class PostDetailView(generic.DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 10


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "blog/user_form.html"
    success_url = reverse_lazy("blog:index")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        fields.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("blog:post-detail", kwargs={"pk": pk})
