from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from blog.models import Post
from .forms import CommentForm


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"post_list": page_obj.object_list, "page_obj": page_obj}

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentaries.all()
        context["form"] = kwargs.get(
            "form", CommentForm(user=self.request.user))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST, user=request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()

            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
