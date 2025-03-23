from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Commentary, Post


class HomePageView(generic.ListView):
    template_name = "blog/index.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits
        context["count_posts"] = context["paginator"].count

        return context

    def get_queryset(self) -> QuerySet:
        return Post.objects.select_related("owner").order_by("-created_time")


class PostsListView(generic.ListView):
    model = Post

    def get_queryset(self) -> QuerySet:
        return Post.objects.select_related("owner").order_by("-created_time")


class PostsDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(generic.CreateView):
    form_class = CommentaryForm
    queryset = Commentary.objects.select_related("user", "post")

    def dispatch(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs["post_pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form) -> any:
        if not self.request.user.is_authenticated:
            form.add_error(None, "Only logged-in users can leave comments.")
            context = {
                "form": form,
                "post": self.post_instance,
            }
            return render(self.request, "blog/post_detail.html", context)

        form.instance.user = self.request.user
        form.instance.post = self.post_instance
        return super().form_valid(form)

    def get_success_url(self):
        return self.post_instance.get_absolute_url()
