# Generated by Django 2.2.11 on 2020-04-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_post_song_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='song_file',
            field=models.FileField(default=0, upload_to='musics/'),
            preserve_default=False,
        ),
    ]
