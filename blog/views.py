from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm
from blog.models import Post


class IndexListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.order_by("-created_time")


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments")
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path
