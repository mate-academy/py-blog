from django import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin


from .models import Post, Commentary


def index(request):
    posts_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj
    }

    return render(request, "blog/index.html", context=context)


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Commentary.objects.filter(post=post)
        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["comments"] = page_obj
        context["form"] = self.get_form()
        return context

    def post(self, request):
        if not request.user.is_authenticated:
            messages.warning(
                request,
                "You need to login to comment this page."
            )
            return redirect("blog:login")
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        post = self.get_object()
        comment = form.save(commit=False)
        comment.post = post
        comment.user = self.request.user
        comment.save()
        return redirect("blog:post_detail", pk=post.pk)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class CustomLoginView(LoginView):
    def get_success_url(self):
        return "/"


class CustomLogoutView(LogoutView):
    next_page = "blog:index"
