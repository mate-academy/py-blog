from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary
from blog.forms import CommentaryForm


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("owner")
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits + 1
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    Post.objects.select_related("owner").prefetch_related("commentaries")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    @staticmethod
    @login_required
    def create_comment_view(
            request: HttpRequest, pk: int
    ) -> HttpResponseRedirect:
        if request.method == "POST":
            form = CommentaryForm(request.POST)
            if form.is_valid():
                Commentary.objects.create(
                    post_id=pk, user=request.user, **form.cleaned_data
                )
        return HttpResponseRedirect(
            reverse_lazy("blog:post-detail", args=(pk,))
        )
