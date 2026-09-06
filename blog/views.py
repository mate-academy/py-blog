from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.annotate(num_comments=Count("comments")).order_by(
        "-created_time"
    )
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = CommentaryForm(user=self.request.user)
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = CommentaryForm(request.POST, user=request.user)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect(self.object.get_absolute_url())

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
