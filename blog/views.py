from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.commentary_set.all().order_by(
            "created_time")
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        if not request.user.is_authenticated:
            messages.error(request, "Увійдіть, щоб додати коментар.")
            return render(request, self.template_name,
                          self.get_context_data())

        content = request.POST.get("content", "").strip()
        if content:
            Commentary.objects.create(post=post, user=request.user,
                                      content=content)
            messages.success(request, "Коментар успішно додано!")
            return redirect("blog:post-detail", pk=post.pk)
        else:
            messages.error(request, "Коментар не може бути порожнім.")
            return render(request, self.template_name,
                          self.get_context_data())
