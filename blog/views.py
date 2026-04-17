from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import CommentaryForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.all().order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "commentary_form" not in context:
            context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to post a comment.")
            return self.render_to_response(
                self.get_context_data(commentary_form=form)
            )

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return HttpResponseRedirect(
                reverse("blog:post-detail", kwargs={"pk": self.object.pk})
            )

        return self.render_to_response(
            self.get_context_data(commentary_form=form)
        )
