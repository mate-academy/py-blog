from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


def login_view(request):
    if request.user.is_authenticated:
        return redirect("blog:index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog:index")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .annotate(
            comment_count=Count("commentaries")
        )
        .order_by("-created_time")
    )


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = (
            self.object.commentaries.select_related("user")
        )
        if "form" not in context:
            context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = self.object
        comment.save()
        return super().form_valid(form)
