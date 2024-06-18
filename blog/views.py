from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.detail import SingleObjectMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.select_related("owner").prefetch_related("commentaries")
    )
    ordering = "-created_time"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryFormView(generic.FormView, SingleObjectMixin):
    form_class = CommentaryForm
    model = Commentary
    template_name = "blog/commentary_form.html"
    success_url = "#"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class PostCommentView(generic.View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentaryFormView.as_view()
        form = CommentaryForm(request.POST)
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/accounts/login/")
        form.instance.user = request.user
        form.instance.post = Post.objects.get(id=self.kwargs["pk"])
        if form.is_valid():
            form.save()
        return view(request, *args, **kwargs)
