from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary, User


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner")


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
        data = super().get_context_data(**kwargs)
        data["form"] = CommentaryForm()
        return data

    @staticmethod
    def post(request: HttpRequest, **kwargs) -> HttpResponse:
        post = Post.objects.get(id=kwargs["pk"])
        form = CommentaryForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post=post,
                **form.cleaned_data
            )
            return HttpResponseRedirect(
                reverse("blog:post-detail", kwargs={"pk": kwargs["pk"]})
            )
        context = {
            "form": form,
            "post": post
        }
        return render(
            request, "blog/post_detail.html", context=context
        )


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
