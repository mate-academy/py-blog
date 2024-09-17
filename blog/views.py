from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": paginator.get_page(page_number),
        "page_obj": page_obj
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        data = super(PostDetailView, self).get_context_data(**kwargs)
        data["comment_form"] = CommentForm
        return data

    def post(self, request, pk=None):
        new_comment = Commentary(
            content=request.POST.get("content"),
            user=self.request.user,
            post=self.get_object(),
        )
        new_comment.save()
        return self.get(self, request)
