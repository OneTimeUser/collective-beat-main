import datetime
from django.contrib.auth import get_user_model
from django.forms.fields import CharField
from django.utils.translation import ugettext as _
from django.forms import ChoiceField, widgets, ModelForm, Form
from django.forms.extras.widgets import SelectDateWidget
from apps.accounts.models import CustomEmailUser, SubscriptionPlans


MIN_AGE_ALLOWED = 10
MAX_AGE_ALLOWED = 100


class CustomSignupForm(ModelForm):
    subscription_plan = ChoiceField(choices=SubscriptionPlans.CHOICES,
                                    widget=widgets.RadioSelect(), label=_('Subscription plan'))
    gender = ChoiceField(choices=CustomEmailUser.GENDER_CHOICES,
                         widget=widgets.RadioSelect(), label=_('Gender'))

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['is_getting_the_news'].label = _('Check to receive news, updates and special offers')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data['gender']

        if self.cleaned_data['gender'] == CustomEmailUser.OTHER and self.cleaned_data['gender_other']:
            user.gender_other = self.cleaned_data['gender_other']

        user.country = self.cleaned_data['country']
        user.birthdate = self.cleaned_data['birthdate']
        user.is_getting_the_news = self.cleaned_data['is_getting_the_news']
        user.subscription_plan = self.cleaned_data['subscription_plan']

        user.save()

        if user.subscription_plan != SubscriptionPlans.FREE:
            user.create_braintree_customer_account()

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'country', 'birthdate', 'gender_other', 'is_getting_the_news')
        widgets = {
            'birthdate': SelectDateWidget(years=range(
                datetime.date.today().year - MIN_AGE_ALLOWED,
                datetime.date.today().year - MAX_AGE_ALLOWED,
                -1
            )),
            'is_getting_the_news': widgets.CheckboxInput()
        }


class AccountEditForm(ModelForm):
    gender = ChoiceField(choices=CustomEmailUser.GENDER_CHOICES,
                         widget=widgets.RadioSelect(), label=_('Gender'))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'gender', 'gender_other', 'email', 'country', 'birthdate')
        widgets = {
            'birthdate': SelectDateWidget(years=range(
                datetime.date.today().year - MIN_AGE_ALLOWED,
                datetime.date.today().year - MAX_AGE_ALLOWED,
                -1
            )),
        }


class EmailSubscriptionForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('is_getting_the_news',)


class ChangeSubscriptionPlanForm(Form):
    payment_method_nonce = CharField()