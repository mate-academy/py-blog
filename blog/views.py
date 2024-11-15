from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from .models import User
from .forms import CommentaryForm

from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]

    queryset = (Post.objects.select_related("owner").
                prefetch_related("commentary_set__user").
                annotate(comment_count=Count("commentary")).
                order_by("-created_time"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_post"] = Post.objects.count()
        context["num_commentary"] = Commentary.objects.count()
        context["num_users"] = User.objects.count()
        return context


class UserListView(generic.ListView):
    model = User
    template_name = "blog/user_list.html"
    context_object_name = "user_list"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    queryset = (Post.objects.
                select_related("owner")
                .prefetch_related("commentary_set__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentary_set.all()
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.post = self.object
                commentary.user = request.user
                commentary.save()
                return redirect("blog:post-detail", pk=self.object.pk)
        else:
            messages.error(request, "You must be logged in to post a comment.")
        return self.render_to_response(self.get_context_data(form=form))
