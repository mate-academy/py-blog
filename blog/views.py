from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentCreateForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    fields = "__all__"
    context_object_name = "post_list"
    queryset = (
        Post.objects.select_related("owner").prefetch_related("commentaries")
    )
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentCreateForm
    queryset = Post.objects.prefetch_related("commentaries__user")

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentCreateForm(initial={"post": self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
