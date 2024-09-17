from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["commentary"] = Commentary.objects.all()

        context["form"] = CommentaryForm(initial={"post": self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, kwargs):
        post_id = kwargs["pk"]
        user = self.request.user
        comment = form.save(commit=False)
        comment.post_id = post_id
        comment.user_id = user.pk
        comment.save()
        return super(PostDetailView, self).form_valid(form)
