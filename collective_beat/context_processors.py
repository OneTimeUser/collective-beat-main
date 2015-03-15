from apps.accounts.models import SubscriptionPlans
from apps.shows.models import Show


def live_show():
    return Show.objects.filter(is_live=True).first()


def cb_context(request):
    context = dict(
        live_show=live_show(),
        SUBSCRIPTION_PLANS=SubscriptionPlans.available_plans_by_ids()
    )
    return context
