from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from blog.models import Post, Commentary
from blog.forms import CommentaryForm, SignUpForm


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    paginate_by = 5
    login_url = "/accounts/login/"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Commentary.objects.filter(
            post=self.object
        ).order_by("-created_time")
        paginator = Paginator(comments, self.paginate_by)
        page = self.request.GET.get("page")
        context["comments"] = paginator.get_page(page)
        context["form"] = CommentaryForm()
        return context


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
