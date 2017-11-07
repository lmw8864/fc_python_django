from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class Photo(models.Model):
    author = models.ForeignKey(User, related_name='photo_posts')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='NoImage.png')

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
            image_obj = Image.open(self.photo)
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
