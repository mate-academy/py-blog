from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    # 1. Передаємо ОФІЦІЙНУ форму в шаблон для звичайного перегляду (GET)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    # 2. Безпечно обробляємо створення коментаря (POST)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Отримуємо поточний пост

        # Заповнюємо форму даними, які прислав користувач
        form = CommentaryForm(request.POST)

        # ПЕРЕВІРКА: чи залогінений користувач І чи форма заповнена правильно
        if request.user.is_authenticated and form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Прив'язуємо коментар до поста
            comment.user = request.user  # Прив'язуємо до автора
            comment.save()  # Тільки тепер зберігаємо в базу даних
            return redirect("blog:post-detail", pk=self.object.pk)

        # Якщо користувач анонім або
        # форма пуста — повертаємо ту саму сторінку з помилками
        context = self.get_context_data(object=self.object)
        context["form"] = form  # Передаємо форму назад, щоб показати помилки
        return self.render_to_response(context)
