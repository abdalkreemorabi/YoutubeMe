# Generated by Django 2.2.11 on 2020-04-12 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='field_name',
            new_name='song_image',
        ),
    ]
