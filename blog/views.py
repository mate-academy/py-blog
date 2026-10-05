from django.db.models import Count
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import AddCommentForm
from blog.models import Post


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = (Post.objects.all().
                annotate(comment_count=Count("commentary")).
                prefetch_related("commentary_set").
                order_by("-created_time"))


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count("commentary"))

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = AddCommentForm()
        pending_comment = self.request.session.pop("pending_comment", "")

        if pending_comment:
            context["form"] = \
                (AddCommentForm(initial={"content": pending_comment}))
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            request.session["pending_comment"] = (request.POST
                                                  .get("content", ""))
            return redirect("/admin/login/?next=%s" % request.path)

        self.object = self.get_object()
        form = AddCommentForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
        else:
            return redirect("blog:post-detail", pk=self.object.pk)
        context = self.get_context_data(object=self.object, form=form)
        return render(request, self.template_name, context)
