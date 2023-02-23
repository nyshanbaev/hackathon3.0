# Generated by Django 4.1.7 on 2023-02-22 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0002_remove_song_image_songimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='musics.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='musics.category')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='musics.song')),
                ('songimage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='musics.songimage')),
            ],
        ),
    ]
