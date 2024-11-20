from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from blog.form import CommentaryForm
from blog.models import Post, Commentary, User


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    paginate_by = 5
    template_name = "post_list.html"
    ordering = ("-created_time",)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_create_form.html"
    success_url = reverse_lazy("blog:index")


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_create_form.html"
    success_url = reverse_lazy("blog:index")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_delete_form.html"
    success_url = reverse_lazy("blog:index")


class UserListView(generic.ListView):
    model = User
    template_name = "blog/autors.html"
    paginate_by = 5

    def get_queryset(self):
        return User.objects.annotate(total_posts=Count("posts"))


class UserDetailView(generic.DetailView):
    model = User
    template_name = "blog/autor_detail.html"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


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
