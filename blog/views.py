from django.shortcuts import redirect, render
from django.views import generic
from django.forms import ModelForm

from blog.models import Commentary, Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related()
    

class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related()

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["form"] = CommentaryForm()
            return context

    def post(self, request, *args, **kwargs):
        return redirect(request.path)


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ("content", )