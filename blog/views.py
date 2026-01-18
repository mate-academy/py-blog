from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from .models import Post, Commentary
from .forms import CommentaryForm


def index(request):
    """View function for the home page of the site."""

    post_list = Post.objects.order_by("-created_time")
    comments = Commentary.objects.all()

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "comments": comments,
        "page_obj": page_obj,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["comments"] = self.object.commentary.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"
