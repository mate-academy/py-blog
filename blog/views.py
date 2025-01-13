from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().select_related("owner")
    paginate_by = 5
    template_name = "blog/index.html"
    context_object_name = "post_list"


class PostDetailView(generic.DetailView, generic.edit.FormMixin):
    template_name = "blog/post_detail.html"
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy("blog:post-detail",
                            kwargs={"pk":self.object.post_id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        post_id = self.object.id
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.post_id = post_id

        self.object.save()

        return super(PostDetailView, self).form_valid(form)
