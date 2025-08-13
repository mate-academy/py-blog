from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Post, Commentary
from .forms import CommentaryForm


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = CommentaryForm()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if not request.user.is_authenticated:
            form.add_error(None, "Only authenticated users can comment.")
            ctx = self.get_context_data(object=self.object)
            ctx["form"] = form
            return self.render_to_response(ctx)

        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post=self.object,
                content=form.cleaned_data["content"],
            )
            return redirect(reverse("blog:post-detail", args=[self.object.pk]))
        ctx = self.get_context_data(object=self.object)
        ctx["form"] = form
        return self.render_to_response(ctx)
