from django.shortcuts import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from .forms import CommentaryForm
from .models import Post


class IndexView(generic.ListView):
    queryset = (Post.objects
                .select_related("owner")
                .prefetch_related("commentaries")
                .order_by("-created_time"))
    paginate_by = 5


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    form_class = CommentaryForm
    queryset = Post.objects.select_related("owner").prefetch_related("commentaries", "commentaries__user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm(self.request.POST or None)
        return context

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return self.form_valid(form=form)
        return self.form_invalid(form=form)
