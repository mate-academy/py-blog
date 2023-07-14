from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .forms import CommentaryForm

from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.all().order_by("-created_time")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    queryset = (
        Post.objects.all().prefetch_related("commentaries").
        select_related("owner")
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = self.request.user
            commentary.post = self.object
            commentary.save()
        return HttpResponseRedirect(self.request.path_info)
