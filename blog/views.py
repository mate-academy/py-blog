from django.views import generic
from django.shortcuts import  redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

@login_required
def commentary_create(request):
    form = CommentaryForm(request.POST or None)
    if form.is_valid():
        commentary = Commentary()
        commentary.user = request.user
        commentary.content = request.POST["content"]
        commentary.post = Post.objects.get(title=request.POST["post"])
        commentary.save()
        return redirect(request.META.get('HTTP_REFERER'))
