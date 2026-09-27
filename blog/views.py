from blog.forms import CommentaryForm
from blog.models import Post, Commentary, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    post = Post.objects.all()
    paginator = Paginator(post, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    contex = {
        "post_list": page_obj,
    }
    return render(request, "blog/home_page.html", context=contex)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    success_url = reverse_lazy("blog:index")
    fields = ["content"]
    template_name = "blog/commentary_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
