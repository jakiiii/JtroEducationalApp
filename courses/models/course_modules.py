import uuid
from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCount
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from courses.models.subject_models import Subject

from jtro_educa.utils import unique_slug_generator
from jtro_educa.utils import upload_image_path

USER = settings.AUTH_USER_MODEL


class CourseQuerySet(models.QuerySet):
    pass


class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)


class Course(models.Model):
    CourseStatus = (
        ('beginner', ' BEGINNER'),
        ('intermediate', 'INTERMEDIATE'),
        ('advance', 'ADVANCED'),
    )
    course_id = models.CharField(unique=True, default=uuid.uuid4, max_length=55)
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='course_created')
    students = models.ManyToManyField(USER, related_name='course_joined', blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    overview = RichTextField()
    image = models.ImageField(upload_to=upload_image_path, default='https://www.nirvanamala.com/frontend/images/noimage.png')
    intro_video = models.FileField(upload_to=upload_image_path, null=True, blank=True)
    total_duration = models.CharField(max_length=20)
    status = models.CharField(choices=CourseStatus, max_length=15)
    file = models.FileField(upload_to=upload_image_path, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    objects = CourseManager()
    tags = TaggableManager()  # django_taggit third party reusable TAG model

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


def courses_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(courses_pre_save_receiver, sender=Course)
