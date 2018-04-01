from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Albums, Songs
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import View

class IndexView(generic.ListView):
    template_name = 'Music/index.html'
    # this query set will be stored in a variable
    # simialar to the model name but in lowercase
    context_object_name = 'albums'
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


# as we are making neither a detail view or list view
# we are inheriting a generic view

class UserFormView(View):
    form_class = UserForm # this variable will contain the basic form skeleton
    # i.e the how the input fields will be there
    template_name = 'Music/registration-form.html'

    # Whenever the form is to be shown to the user
    # empty  file- this method will be called
    def get(self, request):
        form = self.form_class(None)# this is set to None so that we give the user an empty form
        return render(request,self.template_name, {'form': form})# this will give the user an empty form

    # take the data and process it
    def post(self, request):
        # this will take the data from the form
        form = self.form_class(request.POST)
        # Check whether the form is valid

        if form.is_valid():
            user = form.save(commit=False)
            # get the clean username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            user = (authenticate(username=username, password=password))

            #return redirect(reverse('Music:index'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Music:index')

        return render(request, self.template_name, {'form': form})
















