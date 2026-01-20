from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin


from blog.forms import CommentForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentForm(
            initial={"post": self.object, "user": self.request.user}
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)
