from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, Commentary


class PostIndexView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = modelform_factory(Commentary, fields=["content"])
        context["form"] = kwargs.get("form", comment_form())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect("/accounts/login/?next=" + request.path)

        comment_form = modelform_factory(Commentary, fields=["content"])
        form = comment_form(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect(self.object.get_absolute_url())

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
