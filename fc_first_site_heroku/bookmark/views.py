from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bookmark
from django.core.urlresolvers import reverse_lazy

# 동작하는데 로그인이 필요하도록 하려면 아래 클래스를 상속
from django.contrib.auth.mixins import LoginRequiredMixin


class BookmarkList(LoginRequiredMixin, ListView):
    model = Bookmark


class BookmarkDetail(LoginRequiredMixin, DetailView):
    model = Bookmark


class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response(({'form': form}))


class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDelete(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
