from django.core.paginator import Paginator
from django.shortcuts import render, redirect


from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic
from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = (
        Post.objects.prefetch_related("owner")
        .order_by("-created_time")
    )
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"

    def post(
            self,
            request: HttpRequest,
            *args,
            **kwargs
    ) -> HttpResponseRedirect:
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_commentary = form.save(commit=False)
            new_commentary.user = request.user
            new_commentary.post = self.object
            new_commentary.save()
            return redirect(request.path)
        else:
            context = self.get_context_data()
            context["form"] = form
            context["error"] = (
                "Anonymous users cannot post comments. Please log in."
            )
            return render(request, "blog/post_detail.html", context)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context
