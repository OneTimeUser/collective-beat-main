from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.forms import ChoiceField, widgets, ModelForm
from django.forms.extras.widgets import SelectDateWidget
from apps.accounts.models import CustomEmailUser


class CustomSignupForm(ModelForm):
    subscription_plan = ChoiceField(choices=CustomEmailUser.SUBSCRIPTION_TYPE_CHOICES,
                                    widget=widgets.RadioSelect(), label=_('Subscription plan'))
    gender = ChoiceField(choices=CustomEmailUser.GENDER_CHOICES,
                         widget=widgets.RadioSelect(), label=_('Gender'))

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['is_getting_the_news'].label = _('Check to receive news, updates and special offers')

    def signup(self, request, user):
        pass

    class Meta:
        model = get_user_model()
        fields = ('country', 'birthdate', 'is_getting_the_news')
        widgets = {
            'birthdate': SelectDateWidget(),
            'is_getting_the_news': widgets.CheckboxInput()
        }
