from django.contrib import admin
from django.db import models
from orderable.admin import OrderableAdmin
from ckeditor.widgets import CKEditorWidget
from apps.shows.models import ShowCategory, Show


class ShowCategoryAdmin(OrderableAdmin):
    fields = ('title',)


class ShowAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(ShowCategory, ShowCategoryAdmin)
admin.site.register(Show, ShowAdmin)