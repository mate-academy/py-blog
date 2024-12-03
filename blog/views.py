from django.contrib import auth
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.annotate(num_comments=Count("comments")).all().order_by('-created_time')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
        "is_paginated": page_obj.paginator.num_pages > 1,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context["num_comments"] = post.comments.count()
        context["comments"] = post.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={'pk': self.object.pk})

# def logout(request: HttpRequest) -> HttpResponseRedirect:
#     auth.logout(request)
#     return HttpResponseRedirect(reverse_lazy("blog:index"))