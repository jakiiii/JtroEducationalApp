from django.db import models
from django.db.models.signals import pre_save

from jtro_educa.utils import unique_slug_generator


class SubjectQuerySet(models.QuerySet):
    pass


class SubjectManager(models.Manager):
    def get_queryset(self):
        return SubjectQuerySet(self.model, using=self._db)


class Subject(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    objects = SubjectManager()

    class Meta:
        ordering = ('title',)
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.title


def subject_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(subject_pre_save_receiver, sender=Subject)
