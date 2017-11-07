from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # for 함수형 뷰
from django.contrib.auth.mixins import LoginRequiredMixin  # for 클래스형 뷰
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Photo


@login_required
def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'photo/list.html', {'posts': posts})


class UploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('photo', 'text')
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if form.is_valid:
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:post_list')

# reverse_lazy() 및 reverse() 함수는 URL 패턴의 name을 인자로 받습니다. URL 패턴 name을 인식하기 위해서는 urls.py 모듈이 메모리에 로딩되어 있어야 합니다.
# 지금 작성하고 있는 views.py 모듈이 로딩되고 처리되는 시점에 urls.py 모듈이 로딩되지 않을 수도 있으므로, reverse() 대신 reverse_lazy() 를 임포트했습니다.


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    success_url = reverse_lazy('photo:post_list')
    # CreateView 와 UpdateView 는 템플릿을 공유해서 사용  # default = 'photo/photo_form.html'
    template_name = 'photo/upload.html'
