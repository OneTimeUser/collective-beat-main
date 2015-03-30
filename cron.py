#!/usr/bin/env python
import os
import braintree
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collective_beat.settings.local")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import django
django.setup()

from django.contrib.auth import get_user_model
# from django.db import transaction
from apps.accounts.models import SubscriptionPlans


def _clear_user_braintree_data(user_obj):
    user_obj.subscription_plan = SubscriptionPlans.FREE
    user_obj.braintree_subscription_id = None
    user_obj.save()


# @transaction.atomic
def check_expired_subscriptions():
    active_paid_users = get_user_model().objects.exclude(subscription_plan=SubscriptionPlans.FREE)

    for user in active_paid_users:
        if user.braintree_subscription_id:
            user_braintree_subscription = braintree.Subscription.find(user.braintree_subscription_id)

            # https://developers.braintreepayments.com/javascript+python/sdk/server/recurring-billing/overview#statuses
            if user_braintree_subscription.status in [braintree.Subscription.Status.Expired,
                                                      braintree.Subscription.Status.Canceled]:
                _clear_user_braintree_data(user)
        else:
            # cleaning up braintree-related fields for users without 'braintree_subscription_id'
            _clear_user_braintree_data(user)

if __name__ == "__main__":
    check_expired_subscriptions()
