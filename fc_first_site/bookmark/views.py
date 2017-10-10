from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark


class BookmarkList(ListView):
    model = Bookmark


class BookmarkDetail(DetailView):
    model = Bookmark
