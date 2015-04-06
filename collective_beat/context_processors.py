from django.conf import settings
from apps.accounts.models import SubscriptionPlans
from apps.shows.models import Show


def last_show():
    return Show.objects.first()


def cb_context(request):
    context = dict(
        last_show=last_show(),
        SUBSCRIPTION_PLANS=SubscriptionPlans.available_plans_by_ids()
    )

    # settings-file located code blocks to be inserted before closing 'head' and 'body' tags respectively
    try:
        context['HEAD_CLOSING'] = settings.HEAD_CLOSING
        context['BODY_CLOSING'] = settings.BODY_CLOSING
    except AttributeError:
        pass

    return context
