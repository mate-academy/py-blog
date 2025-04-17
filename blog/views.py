from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    )


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context[
            "commentaries"
        ] = self.get_object().commentaries.select_related("user")
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return HttpResponseRedirect(
                reverse(
                    "blog:post-detail",
                    kwargs={"pk": self.object.pk}
                )
            )

        context = self.get_context_data()
        context["form"] = form
        return render(request, "blog/post_detail.html", context=context)
