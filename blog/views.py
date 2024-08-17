from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    paginate_by = 5
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentary_set"))


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentary_set__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentary_form'] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            # Создаем комментарий, не сохраняя его в базу данных
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect('blog:post-detail', pk=self.object.pk)

        context = self.get_context_data(object=self.object)
        context['commentary_form'] = form
        return self.render_to_response(context)

