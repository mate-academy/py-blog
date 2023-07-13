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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        commentary = form.save(commit=False)
        commentary.user = self.request.user
        commentary.post = self.object
        commentary.save()
        return HttpResponseRedirect(self.request.path_info)

    def form_invalid(self, form):
        context = self.get_context_data(commentary_form=form)
        return self.render_to_response(context)
