from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Albums, Songs
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'Music/index.html'

    def get_queryset(self):
        return Albums.objects.all()


class DetailView(generic.DetailView):
    model = Albums
    template_name = 'Music/detail.html'


class AlbumsCreate(CreateView):
    model = Albums
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongsCreate(CreateView):
    model = Songs
    fields = ['album', 'file_type', 'song_title']


class SongsDetail(generic.DetailView):
    model = Songs
    template_name = 'Music/songs_detail.html'


class AlbumsDelete(DeleteView):
    model = Albums
    success_url = reverse_lazy('Music:index')


class SongsDelete(DeleteView):
    model = Songs
    success_url = reverse_lazy('Music:index')


class AlbumsUpdate(UpdateView):
    model = Albums
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'Music/albums_form.html'


class SongsUpdate(UpdateView):
    model = Songs
    fields = ['album', 'file_type', 'song_title']
    template_name = 'Music/songs_form.html'





