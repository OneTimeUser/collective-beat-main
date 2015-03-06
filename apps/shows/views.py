from django.views.generic import ListView
from apps.shows.models import Show


class IndexView(ListView):
    model = Show
    template_name = 'index.html'

    def get_queryset(self):
        return super(IndexView, self).get_queryset()[:1]


class ShowsList(ListView):
    model = Show
    template_name = 'shows/list.html'