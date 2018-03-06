from django.views import generic
from .models import Albums


class IndexView(generic.ListView):
    template_name = 'Music/index.html'

    def get_queryset(self):
        return Albums.objects.all()


class DetailView(generic.DetailView):
    model = Albums
    template_name = 'Music/detail.html'
