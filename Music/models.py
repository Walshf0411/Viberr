from django.db import models
from django.core.urlresolvers import reverse


class Albums(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()

    #This method is called whenever the user adds or updates the entry
	#i.e this is used for redirecting user to a different a page
    def get_absolute_url(self):
        return reverse('Music:detail', kwargs={'pk':self. pk})

    def __str__(self):
        return 'Album : '+str(self.album_title)+' - Artist : '+str(self.artist)


class Songs(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=25)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return 'Song title : '+str(self.song_title)

    def get_absolute_url(self):
        return reverse('Music:detail', kwargs={'pk':self.album.pk})