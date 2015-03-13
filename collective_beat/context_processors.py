from apps.shows.models import Show


def last_show():
    return Show.objects.first()


def cb_context(request):
    context = dict(
        last_show=last_show(),
    )
    return context
