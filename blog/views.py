from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Commentary
from datetime import datetime


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            data["form"] = CommentForm(
                initial={"post": self.object, "user": self.request.user})
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Commentary(content=request.POST.get('content'),
                                 user=self.request.user,
                                 post=self.get_object(),
                                 created_time=datetime.now().strftime(
                                     "%m-%d-%Y, %H:%M:%S")
                                 )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
