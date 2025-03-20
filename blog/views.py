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
        contex = super().get_context_data(**kwargs)
        contex["form"] = CommentaryForm(self.request.POST or None)
        contex["commentaries"] = self.get_object().commentaries.select_related(
            "user"
        )

        return contex

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        context_data = self.get_context_data()
        form = context_data["form"]

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            form.save()
            return HttpResponseRedirect(reverse(
                "blog:post-detail",
                kwargs={"pk": self.object.pk}
            ))
        return render(
            request, "blog/post_detail.html",
            context=context_data
        )
