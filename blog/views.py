from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from blog.forms import CommentForm, SearchForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    context_object_name = "post_list"
    template_name = "blog/index.html"

    def get_queryset(self):
        queryset = (Post.objects.select_related("owner").
                    prefetch_related("comments"))
        title = self.request.GET.get("title")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["search_field"] = SearchForm()
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return (Post.objects.select_related("owner")
                .prefetch_related("comments__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context["counted"] = post.comments.count()
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()

            return HttpResponseRedirect(
                reverse("blog:post-detail", args=(self.object.id,))
            )

        context = {
            "form": form,
            "post": self.object,
        }
        return render(request, self.template_name, context=context)


class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Commentary
    form_class = CommentForm
    template_name = "blog/update_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )


class CommentDeleteView(generic.DeleteView):
    model = Commentary
    template_name = "blog/confirm_delete_form.html"

    def get_success_url(self):
        if self.object.user_id == self.request.user.pk:
            return reverse_lazy(
                "blog:post-detail",
                kwargs={"pk": self.object.post.pk}
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["next"] = self.request.META.get("HTTP_REFERER")
        return context
