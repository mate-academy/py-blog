from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post, Comment


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5



class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect(self.object.get_absolute_url())
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ["content"]
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "blog/comment_form.html"


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()
