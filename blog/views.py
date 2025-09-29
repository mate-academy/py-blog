from django.contrib import messages
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
    all_post = Post.objects.all().order_by('-created_time')

    paginator = Paginator(all_post, 5)  # 5 постів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj.object_list,  # передаємо пагіновані пости
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        form = self.get_form()
        if not request.user.is_authenticated:
            messages.error(
                request,
                'You must log in to post a comment. '
                '<a href="/accounts/login/">Login here</a>.')
            return redirect(self.get_success_url())

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)