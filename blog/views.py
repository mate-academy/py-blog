from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm, PostForm
from blog.models import Post, Commentary


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect(reverse("blog:post-list"))


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_post_form"] = PostForm()
        context["edit_forms"] = {
            post.pk: PostForm(instance=post)
            for post in self.get_queryset()
            if post.owner == self.request.user
        }
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return self.get(request, *args, **kwargs)
        return self.get(request, *args, **kwargs)


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries__user"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_list"] = self.object.commentaries.all()
        context["new_commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            new_commentary = form.save(commit=False)
            new_commentary.user = request.user
            new_commentary.post = self.object
            new_commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_confirm_delete.html"


class CommentaryListView(LoginRequiredMixin, generic.ListView):
    model = Commentary


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary
    template_name = "blog/commentary_confirm_delete.html"

    def get_success_url(self):
        post_id = self.object.post.pk
        return reverse_lazy("blog:post-detail", kwargs={"pk": post_id})
