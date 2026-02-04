from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CommentForm
from django.shortcuts import redirect
# Create your views here.


# @login_required
# def index(request):
#     posts = Post.objects.all().order_by('-created_time')
#
#     return render(request, "blog/index.html", {
#         "posts": posts
#     })


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    login_url = "/accounts/login/"  #

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "comment_form" not in context:
            context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to post a comment.")
            context = self.get_context_data()
            context["comment_form"] = form
            return self.render_to_response(context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content",)
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
