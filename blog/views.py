from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView

from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    # 1. Цей метод додає форму на
    # сторінку, коли ми її просто відкриваємо
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django import forms

        # Створюємо форму прямо тут
        # «на льоту», щоб не створювати файл forms.py
        class SimpleCommentForm(forms.ModelForm):
            class Meta:
                model = Commentary
                fields = ["content"]
                widgets = {
                    "content": forms.Textarea(
                        attrs={"rows": 4, "style": "width: 100%; "
                                                   "max-width: 600px;"}
                    )
                }

        context["form"] = SimpleCommentForm()
        return context

    # 2. Цей метод спрацьовує, коли ти тиснеш кнопку "submit"
    def post(self, request, *args, **kwargs):
        from django.shortcuts import redirect

        post = self.get_object()  # Отримуємо поточний пост
        content = request.POST.get("content")  # Забираємо текст із форми

        if content:
            # Створюємо коментар у базі даних
            Commentary.objects.create(
                content=content,
                post=post,
                user=request.user,  # Прив'язуємо автора коментаря
            )

        # Перезавантажуємо цю ж сторінку, щоб побачити новий коментар
        return redirect("blog:post-detail", pk=post.pk)
