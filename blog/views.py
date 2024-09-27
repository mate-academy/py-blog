from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Post, Commentary, User
from blog.form import CommentaryForm


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content",)
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context["comments"] = Commentary.objects.filter(
            post=self.object
        ).order_by("-created_time")
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return redirect(
                reverse(
                    "blog:post-detail",
                    kwargs={
                        "pk": self.object.pk
                    }
                )
            )
        return self.render_to_response(self.get_context_data(form=form))


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/post_list.html"


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "blog/user_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    success_url = reverse_lazy("blog:comment-create")
    template_name = "blog/post_detail.html"
