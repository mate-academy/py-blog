from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.form import CommentForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comments")
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/accounts/login/")

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()

            return redirect(
                reverse("blog:post-detail", kwargs={"pk": self.object.pk}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
