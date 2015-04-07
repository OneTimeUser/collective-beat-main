from copy import deepcopy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from custom_user.admin import EmailUserAdmin

from apps.accounts.models import CustomEmailUser, SubscriptionBanner, UserSession


class CustomEmailUserAdmin(EmailUserAdmin):
    list_display = ('email', 'get_full_name', 'subscription_plan', 'kickstarter', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'subscription_plan', 'kickstarter', 'groups',)

    def get_fieldsets(self, request, obj=None):
        fs = super(CustomEmailUserAdmin, self).get_fieldsets(request, obj)
        test = list(deepcopy(fs))
        test.insert(1, (_('User info'),
                        {'fields': ('first_name', 'last_name', 'gender', 'country',
                                    'birthdate', 'is_getting_the_news', 'subscription_plan', 'kickstarter')}))

        return tuple(test)

admin.site.register(CustomEmailUser, CustomEmailUserAdmin)
admin.site.register(SubscriptionBanner)
admin.site.register(UserSession)