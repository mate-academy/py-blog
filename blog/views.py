from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from django.db.models import Count
from django.views import generic
from django.urls import reverse_lazy

from models import Post
from forms import CommentaryForm


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        post_list = Post.objects.annotate(
            commentaries_count=Count("commentaries")
        ).order_by("-created_time").select_related("owner")

        paginator = Paginator(post_list, 5)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {"page_obj": page_obj, "post_list": page_obj.object_list}
        return HttpResponse(
            render(request, "blog/index.html", context=context)
        )


class PostDetailView(generic.edit.ModelFormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related(
        "commentaries__user"
    ).select_related("owner")
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def get_initial(self):
        return {"content": None}

    def post(self, request: HttpRequest, *args, **kwargs):
        form = CommentaryForm(request.POST)
        self.object = self.get_object()
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            return super().form_valid(form)

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
