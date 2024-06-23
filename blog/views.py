from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.core.paginator import Paginator

from blog.models import Post
from blog.forms import CommentaryForm


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    content = {
        "page_obj": page_obj,
        "paginator": paginator
    }
    return render(request, "blog/index.html", context=content)


class PostDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form: CommentaryForm) -> HttpResponse:
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if request.user.is_authenticated:
                return self.form_valid(form)
            return redirect("/accounts/login")
        return redirect(request.path)

    def get_success_url(self) -> str:
        return self.request.path
