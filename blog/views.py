from datetime import datetime

from django import forms
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = "-created_time"
    queryset = Post.objects.select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context

    @login_required(login_url="login")
    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        post = self.get_object()
        form = CommentaryForm(request.POST)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = request.user
            commentary.created_time = datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            commentary.save()

            return HttpResponseRedirect(self.request.path_info)

        return self.render_to_response(
            self.get_context_data(post=post, commentary_form=form)
        )


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content", ]
