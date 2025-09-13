from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "post_list": page_obj}
    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if request.user.is_authenticated:
            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.post = self.object
                commentary.user = request.user
                commentary.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return self.form_invalid(form)
