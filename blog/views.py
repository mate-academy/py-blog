from django.contrib.auth import logout
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")\
        .order_by("-created_time")\
        .annotate(num_comments=Count("commentaries"))
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(FormMixin, generic.DetailView):
    queryset = Post.objects.prefetch_related("commentaries__user")
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm(initial={"post": self.object})
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
        return super(PostDetailView, self).form_valid(form)
