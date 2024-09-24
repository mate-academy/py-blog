from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Commentary
from .forms import CommentaryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        context["commentaries"] = Commentary.objects.filter(post=self.object)
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()
            return redirect("blog:post-detail", pk=self.object.pk)
        return self.get(request, *args, **kwargs)


def about_view(request):
    return render(request, "blog/about.html")


def contact_view(request):
    return render(request, "blog/contact.html")
