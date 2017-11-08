from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# https://docs.djangoproject.com/ko/1.11/topics/signals/
from django.db.models.signals import post_delete
from django.dispatch import receiver

from tagging.fields import TagField


class Photo(models.Model):
    author = models.ForeignKey(User, related_name='photo_posts')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='NoImage.png')

    tag = TagField()

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    # Overriding (for 파일 트리가 꼬이는 것을 방지)
    def save(self, *args, **kwargs):
        is_duplicated = False

        if self.photo:
            try:
                before_obj = Photo.objects.get(id=self.id)
                if before_obj.photo == self.photo:
                    is_duplicated = True
            except:
                pass

        if not is_duplicated:
            # image_obj = Image.open(self.photo)
            image_obj = Image.open(self.photo).convert("L")  # 열어서 흑백 모드로 변환 # http://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.convert
            new_image_io = BytesIO()
            image_obj.save(new_image_io, format='JPEG')  # JPEG 포맷으로 저장

            temp_name = self.photo.name
            self.photo.delete(save=False)

            self.photo.save(
                temp_name,
                content=ContentFile(new_image_io.getvalue()),
                save=False
            )

        try:
            before_obj = Photo.objects.get(id=self.id)
            if before_obj.photo == self.photo or is_duplicated:
                self.photo = before_obj.photo
            else:
                before_obj.photo.delete(save=False)
        except:
            pass

        super(Photo, self).save(*args, **kwargs)


# ★★★ 잘못해서 DB의 모든 파일이 다 날아가는 경우가 발생할 수 있으니, 반드시 아래처럼 처리해줘야 합니다! ★★★

@receiver(post_delete, sender=Photo)  # Photo 모델에서 post_delete 시그널이 발생했을 때만 동작
def post_delete(sender, instance, **kwargs):
    storage, path = instance.photo.storage, instance.photo.path
    if (path != '.') and (path != '/') and (path != 'photos/') and (path != 'photos/.'):
        storage.delete(path)
