from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Commentary
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by("created_time")

    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    context = {
        "num_posts": Post.objects.count(),
        "post_list": posts,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["comments"] = self.object.commentary_set.all()
        return context


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    template_name = "blog/commentary_form.html"
    fields = ["content"]
    context_object_name = "commentary"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)
