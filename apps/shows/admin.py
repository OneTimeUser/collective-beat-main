from django.contrib import admin
from orderable.admin import OrderableAdmin
from apps.shows.models import ShowCategory, Show


class ShowCategoryAdmin(OrderableAdmin):
    fields = ('title',)

admin.site.register(ShowCategory, ShowCategoryAdmin)
admin.site.register(Show)