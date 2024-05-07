from django.db.models import Count, Prefetch
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.select_related("owner")
        .annotate(comment_count=Count("commentary"))
        .all()
    )
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView, FormMixin):
    model = Post
    queryset = Post.objects.annotate(
        comment_count=Count("commentary")
    ).prefetch_related(Prefetch("commentary",
                                queryset=Commentary.objects.all()))
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        self.object = self.get_object()
        form = self.form_class(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return self.form_valid(form)

        return self.form_invalid(form)

    # def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         commentary = form.save(commit=False)
    #         commentary.user = request.user
    #         commentary.post = self.object
    #         commentary.save()
    #         return self.form_valid(form)
    #
    #     return self.form_invalid(form)
