from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from .models import Post, Commentary
from .forms import CommentaryForm


def index(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all().order_by('-created_time')

    paginator = Paginator(all_posts, 5)  # 5 постів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,  # передаємо пагіновані пости
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/posts_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:posts-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # отримуємо пост
        if not request.user.is_authenticated:
            return redirect("accounts/login")  # редірект на сторінку логіну

        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)