from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Post, Commentary
from .forms import CommentaryForm


def index(request):
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if request.user.is_authenticated and form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)
