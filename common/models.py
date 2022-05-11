from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(_('Created At'),db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True