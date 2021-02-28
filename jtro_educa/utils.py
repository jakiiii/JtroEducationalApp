import os
import random
import string

from django.utils.text import slugify


# RANDOM STRING GENERATOR FUNCTION
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# UNIQ KEY GENERATOR FUNCTION
def unique_key_generator(instance):
    """
        This is for a Django project with key field.
    """
    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key


# UNIQUE SLUG GENERATOR FUNCTION
def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


# UPLOAD IMAGE METHOD
def get_filename_exist(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(inistance, file_name):
    new_filename = random.randint(1, 101119)
    name, ext = get_filename_exist(file_name)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "/course/%Y/%m/%d/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)
