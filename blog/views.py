from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


def index(request):
    post_list = (Post.objects
                 .select_related("owner")
                 .all()
                 .order_by("-created_time")
                 )

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "post_count": post_list.count(),
        "num_visits": num_visits + 1,
    }

    return render(
        request, "blog/index.html", context=context
    )


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects
                .select_related("owner")
                .prefetch_related("comments__user")
                )


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )


class CommentaryUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
):
    model = Commentary
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.get_object().post.pk}
        )

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user


class CommentaryDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
):
    model = Commentary
    template_name = "blog/commentary_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.get_object().post.pk}
        )

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user
