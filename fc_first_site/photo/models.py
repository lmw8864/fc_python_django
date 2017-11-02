from django.db import models
from django.contrib.auth.models import User


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
