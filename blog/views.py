from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_time").select_related("owner").prefetch_related("commentaries")
    paginate_by = 5
    template_name = "blog/index.html"


class CommentaryCreateView(generic.CreateView):
    # model = Commentary
    # fields = "__all__"
    # template_name = "blog/commentary_form.html"
    # success_url = reverse_lazy("blog:post-detail")
    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = CommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related("commentaries__user")
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

