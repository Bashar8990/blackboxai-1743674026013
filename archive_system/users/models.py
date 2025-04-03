from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', _('Administrator')),
        ('section_admin', _('Section Administrator')),
        ('user', _('Regular User')),
        ('auditor', _('Auditor')),
    ]
    
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name=_('Role')
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name=_('Phone'))
    allowed_sections = models.ManyToManyField(
        'sections.Section',
        blank=True,
        verbose_name=_('Allowed Sections'),
        help_text=_('Sections this user can access')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    def has_section_access(self, section):
        """Check if user has access to a specific section"""
        return self.is_superuser or (self.allowed_sections.filter(id=section.id).exists() and self.is_active)
