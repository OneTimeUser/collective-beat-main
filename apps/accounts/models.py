from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext as _
from custom_user.models import AbstractEmailUser
from django_countries.fields import CountryField


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

    FREE = 'f'
    MONTHLY = 'm'
    ANNUAL = 'a'
    SUBSCRIPTION_TYPE_CHOICES = (
        (FREE, _('Free')),
        (MONTHLY, _('Monthly')),
        (ANNUAL, _('Yearly')),
    )

    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES)
    country = CountryField(_('Country'))
    birthdate = models.DateField(verbose_name=_('Date of Birth'), blank=False, null=True)
    is_getting_the_news = models.BooleanField(default=True, verbose_name='Subscribed to news and updates')
    subscription_plan = models.CharField(max_length=1, choices=SUBSCRIPTION_TYPE_CHOICES)
    braintree_customer_id = models.CharField(max_length=64, null=True, blank=True)

    @cached_property
    def is_paid_member(self):
        return self.subscription_plan in [self.MONTHLY, self.ANNUAL]
