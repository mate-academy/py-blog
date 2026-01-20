from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import CommentaryForm
from .models import Post, Commentary
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related("commentaries")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse_lazy("blog:post-detail", kwargs={"pk": post_id})

        form = CommentaryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
