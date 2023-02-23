# Generated by Django 4.1.7 on 2023-02-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0005_alter_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(upload_to='uploads/author/images'),
        ),
        migrations.AlterField(
            model_name='songimage',
            name='image',
            field=models.ImageField(upload_to='uploads/song/images'),
        ),
    ]
