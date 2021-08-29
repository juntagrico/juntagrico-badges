from django.db import models
from django.utils.translation import gettext as _
from juntagrico.entity.member import Member


class Badge(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True,
                            help_text=_('Eindeutiger Name des Abzeichens'))
    description = models.TextField(_('Beschreibung'), max_length=1000, default='')
    self_assignable = models.BooleanField(_('Selbstauszeichnung'), default=False, help_text=_('Erlaubt Mitglied sich das Abzeichen selbst zu geben'))
    members = models.ManyToManyField(Member, related_name='badges', blank=True, verbose_name=_('Abzeichen'))

    class Meta:
        verbose_name = _('Abzeichen')
        verbose_name_plural = _('Abzeichen')
