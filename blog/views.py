from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, User, Commentary
from blog.forms import RegistrationForm, CommentForm


class IndexView(generic.ListView):
    model = Post
    template_name = "base.html"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailedView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentAddView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        comment.post = post
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class AuthorCreateView(generic.CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("blog:index")
