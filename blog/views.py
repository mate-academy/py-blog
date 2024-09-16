from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.models import Post
from blog.forms import CommentaryForm


class IndexListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm
        return context

    def post(self, request, pk, *args, **kwargs):
        post = self.get_object()
        form = self.get_form()
        user = request.user

        if form.is_valid() and user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()

            return redirect(reverse("blog:post-detail", kwargs={"pk": pk}))

        return redirect("login")
