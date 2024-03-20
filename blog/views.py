from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class Index(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    queryset = Post.objects.prefetch_related("owner").annotate(
        comment_count=Count("commentary")
    )
    paginate_by = 5


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return self.form_valid(form)

        return self.form_invalid(form)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["owner"] = post.owner
        return context
