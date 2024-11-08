from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentaryForm

from .models import Post, Commentary

# from django.core.paginator import Paginator


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().prefetch_related("commentarys")
    for post in posts:
        post.content = post.content[:80] + "..."
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": page_obj.object_list,
        "page_obj": page_obj,
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context=context)


# class PostListView(generic.ListView):
#     model = Post
#     paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("commentarys")


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_form.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/commentary_form.html"

    def post(self, request, *args, **kwargs):
        # return redirect("blog:post-detail", pk=request.POST.get("post"))
        print(request.POST)
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = self.request.user
            commentary.save()
        return redirect("blog:post-detail", pk=kwargs["pk"])


# class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Post
#     from_class = CommentaryForm
#     # fields = "__all__"
#     fields = ["content"]
#     success_url = reverse_lazy("blog:post-detail")
#     template_name = "blog/commentary_form.html"
#     # initial = {"user": "user"}

#     # def get(self, request, *args, **kwargs):
#     #     print(request.GET)
#     #     return super().get(request, *args, **kwargs)

#     # def post(self, request, *args, **kwargs):
#     #     # return redirect("blog:post-detail", pk=request.POST.get("post"))
#     #     print(request.POST)
#     #     return redirect("blog:post-detail", pk=kwargs["pk"])

#     def form_valid(self, form):
#         print(self.request.POST)
#         # print(self.request.kwargs)
#         # print(self.get_object())
#         # print(self.request.GET.get("id"))
#         commentary = form.save(commit=False)
#         commentary.post = self.get_object()
#         commentary.user = self.request.user
#         commentary.save()
#         return super().form_valid(form)

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     id = self.request.GET.get("id")
#     #     context["id"] = id
#     #     return context
