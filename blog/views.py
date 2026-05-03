from django.db.models import Count, Prefetch
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    paginate_by = 5

    def get_queryset(self):
        return (
            Post
            .objects
            .select_related("owner")
            .annotate(
                comment_amount=Count(
                    "commentaries",
                    distinct=True
                )
            )
            .order_by("-created_time")
        )


class PostDetailView(generic.DetailView):
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            request.session["comment_content"] = request.POST.get("content")
            form.add_error(None, "You must be logged in to be able to comment")
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = self.request.user
            comment.save()
            return redirect(request.path)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_queryset(self):
        return (
            Post
            .objects
            .select_related("owner")
            .prefetch_related(
                Prefetch(
                    "commentaries",
                    queryset=Commentary.objects.select_related("user")
                )
            )
            .annotate(
                comment_amount=Count(
                    "commentaries",
                    distinct=True
                )
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if "form" not in context:
            initial = {}

            content = self.request.session.pop("comment_content", None)

            if content:
                initial["content"] = content

            context["form"] = CommentForm(initial=initial)

        context["comments"] = self.object.commentaries.all()
        return context
