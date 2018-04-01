from django.conf.urls import url
from . import views

app_name = 'Music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^albums/add/$', views.AlbumsCreate.as_view(), name='album-create'),
    url(r'^albums/addsongs/$', views.SongsCreate.as_view(), name='song-create'),

    url(r'albums/song/(?P<pk>[0-9]+)/$', views.SongsDetail.as_view(), name='song-detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'albums/song/(?P<pk>[0-9]+)/delete/$', views.SongsDelete.as_view(), name='song-delete'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumsDelete.as_view(), name='album-delete'),

    url(r'^(?P<pk>[0-9]+)/update/$', views.AlbumsUpdate.as_view(), name='album-update'),
    url(r'albums/song/(?P<pk>[0-9]+)/update/$', views.SongsUpdate.as_view(), name='song-update'),
]