from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.forms import CommentCreate
from blog.models import Post, Commentary


def index(request):
    posts = Post.objects.all().prefetch_related("commentaries").order_by("-created_time")

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": paginator.get_page(page_number),
        "page_obj": page_obj,
    }

    return render(request=request, template_name="blog/index.html", context=context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentCreate

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            Commentary.objects.create(
                user=request.user,
                content=request.POST["content"],
                post_id=kwargs["pk"]
            )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)
