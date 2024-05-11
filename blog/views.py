from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.models import Post, Commentary


def index(request):
    """View function for the home page of the site."""
    posts = (
        Post.objects.select_related("owner")
        .annotate(number_of_comments=Count("commentaries"))
        .order_by("-created_time")
    )

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "post_list": posts,
    }
    return render(request, "blog/index.html", context=context)


class CommentaryForm(forms.ModelForm):
    """Made to be a mixin in PostDetailView to add detailed view of comments"""

    class Meta:
        model = Commentary
        fields = [
            "content",
        ]


class PostDetailView(DetailView, FormMixin):
    """Detailed view + form in the same class"""
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        comments = (
            post.commentaries
            .select_related("user")
            .order_by("created_time")
        )
        paginator = Paginator(comments, 10)
        page_number = self.request.GET.get("page")
        try:
            comments = paginator.page(page_number)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        context["comments"] = comments
        context["form"] = self.get_form()
        return context

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        PostDetailView.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
