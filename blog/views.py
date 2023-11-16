from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary
from django.contrib.auth.mixins import LoginRequiredMixin


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


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ['content']
    template_name = 'blog/commentary_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.kwargs['pk']})
