from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count, Prefetch
from django.views.generic.edit import FormMixin

from .forms import CommentaryForm
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = (
        Post.objects.select_related("owner")
        .annotate(num_comments=Count("commentaries"))
    )


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm
    queryset = Post.objects.prefetch_related(
        Prefetch(
            "commentaries",
            queryset=Commentary.objects.select_related("user")
        )
    ).annotate(num_comments=Count("commentaries"))

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
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
