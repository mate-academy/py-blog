from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Commentary
from .forms import CommentaryForm


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:index")


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Commentary.objects.filter(post=post).order_by("-created_time")
        context = {
            "post": post,
            "comments": comments,
        }
        if request.user.is_authenticated:
            context["form"] = CommentaryForm()
        return render(request, "blog/post_detail.html", context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Commentary.objects.filter(post=post).order_by("-created_time")
        context = {
            "post": post,
            "comments": comments,
        }
        if request.user.is_authenticated:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.post = post
                commentary.user = request.user
                commentary.save()
                print("Redirecting to post detail after comment save")
                return HttpResponseRedirect(reverse("blog:index"))
            context["form"] = form
        else:
            form = CommentaryForm(request.POST)
            form.add_error(None, "You must be logged in to post a comment.")
        return render(request, "blog/post_detail.html", context)
