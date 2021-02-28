from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from ckeditor.fields import RichTextField

from jtro_educa.utils import upload_image_path


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(self._meta.model_name), {'item': self})


class Text(ItemBase):
    content = RichTextField()


class File(ItemBase):
    file = models.FileField(upload_to=upload_image_path)


class Image(ItemBase):
    image = models.ImageField(upload_to=upload_image_path)


class Video(ItemBase):
    url = models.URLField
