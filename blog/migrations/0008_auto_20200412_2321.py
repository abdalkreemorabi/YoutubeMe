# Generated by Django 2.2.11 on 2020-04-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200412_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='song_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
