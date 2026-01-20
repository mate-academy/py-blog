from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class MainPageView(generic.ListView):
    model = Post
    queryset = (Post.objects.select_related("owner")
                .annotate(num_comments=Count("comments")))
    context_object_name = "post_list"
    paginate_by = 5
    template_name = "blog/main_page.html"


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context["num_comments"] = post.comments.count()
        context["comments"] = post.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})
