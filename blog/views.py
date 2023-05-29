from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from blog.models import Post, Commentary, User
from blog.forms import CommentaryForm


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_users = User.objects.count()
        num_posts = Post.objects.count()
        page = self.request.GET.get("page", 1)
        paginator = Paginator(self.object_list, self.paginate_by)
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        context["num_users"] = num_users
        context["num_posts"] = num_posts
        context["page"] = page
        context["post_list"] = post_list
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={
            "pk": self.object.id
        })

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
        return self.form_invalid(form)
