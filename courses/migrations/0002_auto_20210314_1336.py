# Generated by Django 2.2 on 2021-03-14 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='author',
            new_name='owner',
        ),
    ]
