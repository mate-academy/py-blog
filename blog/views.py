from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, User, Commentary


def index(request: HttpRequest) -> HttpResponse:
    all_post = (
        Post.objects.all()
        .order_by("-created_time")
        .select_related("owner")
        .prefetch_related("commentaries")
    )

    paginate_by_str = request.GET.get("paginate_by", "5")

    try:
        paginate_by = int(paginate_by_str)
    except ValueError:
        paginate_by = 5

    paginator = Paginator(all_post, paginate_by)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "paginate_by": paginate_by,
        "post_list": page_obj.object_list,
    }

    return render(request, "blog/index.html", context=context)


class BlogDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm

    def form_valid(self, form):
        post_id = self.request.POST.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        commentary = form.save(commit=False)
        commentary.post = post
        commentary.user = self.request.user
        commentary.save()
        return redirect("blog:post-detail", pk=post.id)
