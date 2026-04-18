from crispy_forms.helper import FormHelper
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    def __init__(self) -> None:
        super().__init__()
        self.helper = FormHelper()
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
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
        comment = form.save(commit=False)
        comment.post = Post.objects.get(pk=self.object.pk)
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})
