from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ("-created_time",)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.commentaries.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = self.object
                new_comment.user = request.user
                new_comment.save()
                new_comment.save(update_fields=["user", "post"])
                return HttpResponseRedirect(reverse("blog:index"))
            else:
                messages.error(request, "Your data is not valid")
        else:
            messages.error(request, "You have to login")


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentForm
    success_url = reverse_lazy("blog:index")
