from django.db import models
from django.utils.translation import gettext_lazy as _

class Section(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['name']

    def __str__(self):
        return self.name
