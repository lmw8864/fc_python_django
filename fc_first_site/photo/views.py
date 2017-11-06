from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # for 함수형 뷰
from .models import Photo


@login_required
def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'photo/list.html', {'posts': posts})
