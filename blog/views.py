from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return (
            Post.objects.select_related("owner")
            .annotate(comment_count=Count("commentaries"))
            .order_by("-created_time")
        )


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return Post.objects.select_related("owner").prefetch_related(
            "commentaries__user"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(
            request.POST,
            user=request.user,
            post=self.object
        )
        if form.is_valid():
            form.save()
            return redirect(self.object.get_absolute_url())
        context = self.get_context_data(form=form)
        return self.render_to_response(context)
