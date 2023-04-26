from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.all().prefetch_related("owner__commentaries")


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"
    queryset = Post.objects.all().prefetch_related("owner__commentaries")

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["form"] = self.form_class()
        return context

    # def post(self, request, *args, **kwargs):
    #     self.success_url = reverse_lazy("blog:post-detail", kwargs={"pk": kwargs["pk"]})
    #     # form = self.form_class(request.POST)
    #     # if form.is_valid():
    #     #     return self.form_valid(form)
    #     return super().post(request, *args, **kwargs)

    # def form_valid(self, form):
    #     # commentary = form.save(commit=False)
    #     # commentary.user = self.request.user
    #     # commentary.post = self.get_object()
    #     # commentary.save()
    #     # super().form_valid(form)
    #     form.initial["user"] = self.request.user
    #     form.initial["post"] = self.get_object()
    #     return super().form_valid(form)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/commentary_form.html"
    queryset = Commentary.objects.all().prefetch_related("user__posts")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            comment = form.save(commit=False)
            comment.user = user
            comment.post = Post.objects.get(id=kwargs["pk"])
            comment.save()
        return redirect(reverse("blog:post-detail", args=[kwargs["pk"]]))
