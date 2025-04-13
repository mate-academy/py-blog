from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryCreateForm
from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    # context_object_name = "post_list"
    # template_name = "blog/post_list.html"
    paginate_by = 5


# class PostDetailView(LoginRequiredMixin, DetailView):
#     model = Post
#     # queryset = Post.objects.all().select_related("comments")
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["commentary_form"] = CommentaryForm()
#         return context


#
# class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Commentary
#     form_class = CommentaryForm
#     success_url = reverse_lazy("blog:post-detail")
#
#     def post(self, request, *args, **kwargs):
#         post = get_object_or_404(Post, pk=request.POST.get("post_id"))
#         form = CommentaryCreateView.form_class(request.POST)
#         commentary_form = CommentaryForm()
#         if form.is_valid():
#             commentary = form.save(commit=False)
#             commentary.post = post
#             commentary.user = request.user
#             commentary.save()
#             # return redirect("blog:post-detail", pk=post.id)
#         context = {
#             "post": post,
#             "form": form,
#             "commentary_form": commentary_form
#         }
#         return render(request, "blog/post_detail.html", context)


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by("-created_time")


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        context = {"form": CommentaryCreateForm(), "post": post}

        return render(request, "blog/post_detail.html", context)

    def post(self, request: HttpRequest, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)

        form = CommentaryCreateForm(request.POST)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = post
            commentary.save()

            if request.headers.get("HX-Request"):
                return render(
                    request,
                    "blog/partials/single_commentary.html",
                    {"commentary": commentary},
                )

            return redirect(post.get_absolute_url())

        context = {"form": form, "post": post}

        return render(request, "blog/post_detail.html", context)
