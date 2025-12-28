from django import forms
from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, Comment


class HomePageListView(generic.ListView):
    model = Post
    template_name = "main/post_list.html"
    context_object_name = "post_list"
    ordering = "-created_time"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
