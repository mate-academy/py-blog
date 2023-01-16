from blog.models import Post, Commentary, User
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class Index(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    context_object_name = "post_list"
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentaries"))


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/comment_create.html"

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.post = Post.objects.get(id=self.request.GET["pk"])
        fields.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        if "invalid_form" in self.request.META.get("HTTP_REFERER"):
            return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))
        return HttpResponseRedirect(
            f"{self.request.META.get('HTTP_REFERER')}?invalid_form=True"
        )

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.request.GET["pk"]})


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]
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

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk": self.kwargs["pk"]})


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
