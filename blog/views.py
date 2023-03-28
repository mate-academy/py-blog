from blog.forms import CommentForm
from blog.models import Post, Commentary
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views import generic


def index(request):
    posts = Post.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(posts, 5)

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "commentary_set").select_related("owner").order_by(
        "created_time"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            Commentary.objects.create(
                **form.cleaned_data,
                post_id=self.object.pk,
                user_id=self.request.user.id
            )
            return redirect("blog:post-detail", pk=self.object.pk)
        else:
            return render(request, "")
