from django.db import models

from ckeditor.fields import RichTextField

from courses.models.course_modules import Course
from courses.fields import OrderField


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return '{}.{}'.format(self.order, self.title)

    class Meta:
        ordering = ['order']
