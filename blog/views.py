from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin, CreateView, ProcessFormView

from blog.form import CommentaryForm
from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = "-created_time"
    queryset = Post.objects.all().select_related("owner")
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(comment_count=Count("commentaries"))
        return queryset


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_success_url(self):
      #  print("TEST get_success_url!!!!!!!!!!!!!!!")
       return reverse_lazy("blog:post-detail", kwargs={"pk": self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["post"] = Post.objects.get(pk=self.kwargs["pk"])
        context["user"] = self.request.user
        context["comments"] = Commentary.objects.filter(post=self.object)
        return context

    def post(self, request, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print("!!!!!!!!!!!!!!!!!!!!TEST def post()!!!!!!!!!!!!!!!!!!!")
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        print("##########111111111111##########")
        form.instance.post = self.object
        print("##########2222221111111##########")
        form.instance.author = self.request.user
        print("##########13333333111111##########")
        form.save()
        print("!!!!!!!!!!!!!!!!!!!TEST!!!!!!!!!!!!! form_valid")
        return super(PostDetailView, self).form_valid(form)
