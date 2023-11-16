from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary

from django.shortcuts import get_object_or_404


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ['content']
    template_name = 'blog/commentary_create.html'
    success_url = reverse_lazy('blog:post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
