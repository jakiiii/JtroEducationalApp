from django.contrib import admin
from .models.subject_models import Subject
from .models.course_modules import Course
from .models.module_models import Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'author', 'price', 'status', 'active', 'featured', 'created']
    list_filter = ['created', 'featured', 'subject']
    search_fields = ['title', 'subject', 'author', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
