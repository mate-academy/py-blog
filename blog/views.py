from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView, CreateView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def index(request: HttpRequest) -> HttpResponse:
    page_size = 5
    all_posts = Post.objects.all().order_by("created_time")
    paginator = Paginator(all_posts, page_size)
    page_number = request.GET.get("page")
    try:
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)
    context = {
        "all_posts": paginated_posts
    }
    return render(
        request,
        "blog/index.html",
        context=context
    )


class PostDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.commentary_set.all()
        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context["comments"] = page_obj
        return context


class CommentaryListView(LoginRequiredMixin, generic.ListView):
    model = Commentary
    paginate_by = 5


class CommentaryCreateView(LoginRequiredMixin, FormView):
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def form_valid(
        self,
        form: CommentaryForm
    ) -> HttpResponseRedirect:
        post = Post.objects.get(pk=self.kwargs["pk"])
        Commentary.objects.create(post=post, user=self.request.user, content=form.cleaned_data["content"])
        return super().form_valid(form)

    def get_success_url(self) -> HttpResponse:
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.kwargs["pk"]})
