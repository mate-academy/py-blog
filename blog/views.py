from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import redirect
from blog.forms import CommentaryForm
from blog.models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = (
        Post.objects.
        select_related("owner").
        prefetch_related("comments").
        all()
    )
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.get_object().id)
        context = self.get_context_data(object=self.get_object(), form=form)
        return self.render_to_response(context)
