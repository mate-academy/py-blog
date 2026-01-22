from django.core.paginator import Paginator
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"post_list": page_obj}
    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            form.add_error(None, "You must be logged in to comment.")
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = self.request.user
            commentary.save()
            return redirect(self.object.get_absolute_url())
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return self.render_to_response(context)


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
