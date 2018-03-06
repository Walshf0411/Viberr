from django.db import models
from django.core.urlresolvers import reverse


class Albums(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('Music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Album : '+str(self.album_title)+' - Artist : '+str(self.artist)


class Songs(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=25)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return 'Song title : '+str(self.song_title)
