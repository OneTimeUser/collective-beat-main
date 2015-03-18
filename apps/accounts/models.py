from django.conf import settings
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext as _
from custom_user.models import AbstractEmailUser
from django_countries.fields import CountryField
from allauth.account.models import EmailAddress


class SubscriptionPlans(object):
    FREE = 'f'
    MONTHLY = 'm'
    ANNUAL = 'a'

    CHOICES = (
        (FREE, _('Free')),
        (MONTHLY, _('Monthly')),
        (ANNUAL, _('Yearly')),
    )

    PLAN_PRICE_DESCRIPTION = {
        FREE: _('Limited opportunities'),
        MONTHLY: _('$5/month'),
        ANNUAL: _('$50/year')
    }

    @classmethod
    def available_plans(cls):
        result = []
        for plan_data in cls.iter_available_plans():
            result.append(plan_data)

        return result

    @classmethod
    def available_plans_by_ids(cls):
        result = {}
        for plan_data in cls.iter_available_plans():
            result[plan_data['id']] = plan_data

        return result

    @classmethod
    def iter_available_plans(cls):
        for plan_id, title in cls.CHOICES:
            yield {
                'id': plan_id,
                'title': title,
                'description': cls.PLAN_PRICE_DESCRIPTION[plan_id],
            }

    @classmethod
    def get_paid_plans(cls):
        return [cls.MONTHLY, cls.ANNUAL]


class CustomEmailUser(AbstractEmailUser):
    """
    Extanding EmailUser custom_user
    """
    MALE = 'm'
    FEMALE = 'f'
    OTHER = 'o'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (OTHER, _('Other')),
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
    gender_other = models.CharField(_('gender (other)'), max_length=30, blank=True, null=True)
    country = CountryField(_('country'))
    birthdate = models.DateField(verbose_name=_('Date of Birth'), blank=False, null=True)
    is_getting_the_news = models.BooleanField(default=True, verbose_name='Subscribed to news and updates')
    subscription_plan = models.CharField(max_length=1, choices=SubscriptionPlans.CHOICES)
    braintree_customer_id = models.CharField(max_length=64, null=True, blank=True)

    @cached_property
    def is_paid_member(self):
        return self.subscription_plan in SubscriptionPlans.get_paid_plans()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return super(CustomEmailUser, self).get_full_name()

    @cached_property
    def get_subscription_plans_info(self):
        result = {
            'current': None,
            'available': []
        }

        for plan_data in SubscriptionPlans.iter_available_plans():
            if plan_data['id'] == self.subscription_plan:
                result['current'] = plan_data
            else:
                result['available'].append(plan_data)

        return result

    def __unicode__(self):
        return self.get_full_name()


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user)

    class Meta:
        db_table = 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

CustomEmailUser.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

