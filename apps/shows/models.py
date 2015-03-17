import re
import os
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.files.storage import default_storage
from unicodedata import normalize
from orderable.models import Orderable

_filename_ascii_strip_re = re.compile(r'[^A-Za-z0-9_.-]')


def secure_filename(filename):
    if isinstance(filename, basestring):
        filename = normalize('NFKD', filename).encode('ascii', 'ignore')
    filename = str(_filename_ascii_strip_re.sub('', '_'.join(
                   filename.split()))).strip('._')
    filename = default_storage.get_valid_name(filename)
    filename = default_storage.get_available_name(filename)

    return filename


def upload_to(instance, filename):
    filename = secure_filename(filename)
    table = instance._meta.db_table
    date = timezone.now().strftime('%Y/%m/%d')

    return os.path.join(table, date, filename)


class ShowCategory(Orderable):
    title = models.CharField(_('Show title'), max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('categories')


class Show(models.Model):
    category = models.ManyToManyField(ShowCategory)
    title = models.CharField(_('Show title'), max_length=255)
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    image = models.ImageField()
    url = models.CharField(max_length=255)
    url_for_ios = models.CharField(max_length=255)
    date = models.DateField()
    show_number = models.CharField(max_length=20)
    is_live = models.BooleanField(default=False)

    def __unicode__(self):
        return 'SILENCIO {}: {}'.format(self.show_number, self.title)

    class Meta:
        ordering = ('-date',)
