from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Post, Commentary
from django.core.paginator import Paginator
from django.views import generic
from .forms import CommentaryForm


def index(request):
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", {
        "post_list": page_obj.object_list,
        "page_obj": page_obj
    })


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Commentary.objects.filter(
            post=self.object
        ).order_by("-created_time")
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
