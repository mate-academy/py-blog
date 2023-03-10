from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post

