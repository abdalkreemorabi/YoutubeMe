# Generated by Django 2.2.11 on 2020-04-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200416_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='song_file',
            field=models.FileField(null=True, upload_to='musics/'),
        ),
    ]