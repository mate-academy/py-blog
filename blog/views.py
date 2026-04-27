from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = (
        Post.objects
        .all().select_related("owner").prefetch_related("comments")
    )


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        # 1. Проверяем аутентификацию пользователя (требование п. 19)
        if not request.user.is_authenticated:
            # Если пользователь не залогинен, форма считается невалидной.
            # В данном случае перенаправляем на логин или возвращаем
            # ту же страницу.
            return redirect("login")

        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        # 2. Проверяем валидность данных формы
        if form.is_valid():
            # 3. Создаем экземпляр без сохранения в БД,
            # чтобы добавить автора и пост
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            # Сохраняем в базу данных
            commentary.save()

            # 4. Перенаправляем обратно на страницу с деталями поста
            return redirect("blog:post-detail", pk=self.object.pk)

        # Если форма невалидна, возвращаем страницу с ошибками
        context = self.get_context_data(object=self.object)
        context["commentary_form"] = form
        return self.render_to_response(context)
