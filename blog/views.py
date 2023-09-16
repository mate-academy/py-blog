from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .models import Post
from .forms import CommentaryForm, PostForm
from django import forms


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    context_object_name = "post"
    form_class = CommentaryForm

    def get_success_url(self) -> str:
        return reverse("blog:post-detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs) -> dict:
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentaryForm(initial={
            "post": self.object,
            "user": self.request.user
        })
        form.fields["post"].widget = forms.HiddenInput()
        form.fields["user"].widget = forms.HiddenInput()
        form.fields["content"].label = "Add new comment"
        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if not request.user.is_authenticated:
            return self.form_invalid(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ("title", "content")

    # return to index after creation
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



