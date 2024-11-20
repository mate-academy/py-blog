from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    DeleteView
)
from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = "-created_time"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["paginator"] = self.get_paginator(
            self.get_queryset(), self.paginate_by
        )
        context["page_obj"] = self.get_page()
        return context

    def get_page(self):
        page_number = self.request.GET.get("page")
        paginator = self.get_paginator(self.get_queryset(), self.paginate_by)
        return paginator.get_page(page_number)


class PostDetailView(DetailView, FormView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentaryForm
    success_url = reverse_lazy("blog:post-detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.save()
            return redirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form))


class AddCommentView(CreateView):
    model = Commentary
    form_class = CommentaryForm

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"pk": self.kwargs["pk"]}
        )


class CommentaryDeleteView(DeleteView):
    model = Commentary
    template_name = "blog/commentary_confirm_delete.html"

    def get_success_url(self):
        post_id = self.object.post.pk
        return reverse_lazy("blog:post-detail", kwargs={"pk": post_id})
