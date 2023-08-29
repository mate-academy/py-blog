from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_initial(self):
        return {
            "user": self.request.user,
            "post": self.object
        }

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = self.get_form()
        # print(context)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
