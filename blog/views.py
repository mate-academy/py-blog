from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic


from blog.models import Post, Commentary
from blog.forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/blog_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"


class AddCommentView(generic.CreateView):
    model = Commentary
    template_name = "blog/add_comment.html"
    # fields = "__all__"
    form_class = CommentaryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    success_url = reverse_lazy("blog:post-detail")


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/comment_form.html"




# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentaryForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentaryForm()
#
#     context = {'post': post,
#                'comments': comments,
#                'new_comment': new_comment,
#                'comment_form': comment_form}
#
#     return render(request, "blog/comment_form.html", context=context)