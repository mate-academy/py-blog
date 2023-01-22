from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin, ProcessFormView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    paginate_by = 5
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    ).annotate(num_comments=Count("commentaries"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if "num_visits" in self.request.session:
            self.request.session["num_visits"] += 1
        else:
            self.request.session["num_visits"] = 1
        context["num_visits"] = self.request.session.get("num_visits", 1)
        return context


# def post_detail_view(request, pk):
#     post = Post.objects.get(id=pk)
#     context = {"post": post}
#     form = CommentaryForm(request.POST or None)
#     if form.is_valid():
#         content = request.POST.get("content")
#         Commentary.objects.create(
#             post=post,
#             user=request.user,
#             content=content
#         )
#         return HttpResponseRedirect(reverse("blog:index"))
#         # return redirect("blog:index")
#     context["form"] = form
#     return render(request, "blog/post_detail.html", context=context)


class PostDetailView(FormMixin, ProcessFormView, generic.DetailView):
    form_class = CommentaryForm
    model = Commentary
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:index")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = Post.objects.get(pk=self.get_object().id)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post"] = Post.objects.get(pk=self.get_object().id)
    #     context["user"] = self.request.user
    #     return context

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # context["form"] = CommentaryForm(initial={"post": self.object})
        context["post"] = Post.objects.get(pk=self.get_object().id)
        context["user"] = self.request.user
        return context
