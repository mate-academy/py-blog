from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import DetailView

from blog.forms import CommentaryForm
from blog.models import Post


def index(request):
    posts = Post.objects.order_by("-created_time")
    paginator = Paginator(posts, 5)  # 5 постів на сторінку

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/index.html", {
        "page_obj": page_obj,
        "post_list": page_obj.object_list
    })


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "comment_form" not in context:
            context["comment_form"] = CommentaryForm(
                initial={"user": self.request.user}
            )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST, initial={"user": request.user})

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()

            return redirect("blog:post-detail", pk=self.object.pk)
        else:
            context = self.get_context_data(object=self.object)
            context["comment_form"] = form
            return self.render_to_response(context)
