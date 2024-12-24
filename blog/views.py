from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView
from blog.models import Post, Commentary
from django import forms


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Add Commentary"}


class HomeView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all().order_by("-created_time")
    queryset.prefetch_related("commentaries")


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("owner")
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        post = self.get_object()
        content["comments"] = post.commentaries.all()
        content["form"] = CommentaryForm()
        return content

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = user
            commentary.post = post
            commentary.save()
            return HttpResponseRedirect(self.request.path_info)
