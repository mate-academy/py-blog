from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from .models import User, Post, Commentary
from django.views.generic.edit import FormMixin


@login_required
def index(request):
    """View function for the home page of the site."""

    num_users = User.objects.count()
    num_posts = Post.objects.count()
    num_commentaries = Commentary.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_posts": num_posts,
        "num_commentaries": num_commentaries,
        "num_visits": num_visits + 1,
    }

    return render(request, "blog/index.html", context=context)


class CommentaryListView(generic.ListView):
    model = Commentary
    context_object_name = "commentary_list"
    template_name = "blog/commentary_list.html"
    ordering = ["-created_time"]
    paginate_by = 5


class CommentaryDetailView(generic.DetailView):
    model = Commentary
    template_name = "blog/commentary_detail.html"


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    ordering = ["created_time"]
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
