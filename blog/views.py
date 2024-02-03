from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView

from blog.models import Post
from .forms import CreateCommentary, RegisterForm


def index(request):
    queryset = (
        Post.objects.select_related("owner")
        .annotate(Count("commentaries"))
        .order_by("-created_time")
    )
    paginator = Paginator(queryset, 5)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(
        request,
        "blog/index.html",
        {"post_list": page_obj, "page_obj": page_obj},
    )


class PostDetailView(DetailView):
    model = Post

    def get_object(self):
        return (self.model.objects.select_related("owner")
                .get(pk=self.kwargs["pk"]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentaries.prefetch_related("user")
        paginator = Paginator(self.object.commentaries
                              .prefetch_related("user"), 2)
        context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
        context["form"] = CreateCommentary({"post": self.object.pk})
        return context


class CommentCreate(View):
    def post(self, request):
        form = CreateCommentary(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
        return redirect(request.META.get("HTTP_REFERER"))


class RegistrateUserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("login")
    extra_context = {"is_registration": True}


def log_out(request):
    logout(request)
    return redirect(request.META.get("HTTP_REFERER"))
