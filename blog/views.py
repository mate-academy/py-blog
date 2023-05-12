from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryCreateForm
from blog.models import Commentary, Post


def index(request):
    post_list = Post.objects.all()
    num_commentary = Commentary.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "post_list": post_list,
        "num_commentary": num_commentary,
        "num_visits": num_visits + 1,
    }

    return render(request, "blog/index.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post


class CommentaryDetailView(generic.DetailView):
    model = Commentary

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().select_related("owner").prefetch_related("commentaries")
    paginate_by = 5


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):

    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = CommentaryCreateForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

            return HttpResponseRedirect(post_url)
