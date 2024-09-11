from django.views import generic

from blog.models import Post


class BlogListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner").order_by("-created_time")
    )


class PostDetailView(generic.DetailView):
    model = Post
