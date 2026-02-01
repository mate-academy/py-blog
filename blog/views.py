from django import forms
from django.core.paginator import Paginator
from django.db.models import Prefetch, Count
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    all_posts = (Post.objects.select_related("owner")
                 .annotate(num_comments=Count("comments"))
                 .order_by("-created_time"))

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page", 1)
    paginated_posts = paginator.get_page(page_number)
    context = {
        "page_obj": paginated_posts,
        "post_list": paginated_posts.object_list
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        Prefetch(
            "comments",
            queryset=Commentary.objects.select_related("user")
        )
    )
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentaryForm(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = self.object
                comment.user = request.user
                comment.save()
                return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": ""}
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Write your comment here..."
            }),
        }
