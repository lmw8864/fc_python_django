from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # for 함수형 뷰
from django.contrib.auth.mixins import LoginRequiredMixin  # for 클래스형 뷰
from django.views.generic import CreateView
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
