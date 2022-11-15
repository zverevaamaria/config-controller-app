from django.db import models
from django.utils import timezone
import datetime

class Config(models.Model):
    service = models.CharField('сервис конфига', max_length=200,  null=True, unique=True, blank=True)
    data = models.JSONField('содержимое конфига', blank=False)
    version = models.DecimalField('версия конфига', blank=True, decimal_places=2, max_digits=5, default=1)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField('дата создания конфига',  default=timezone.now)
    updated_at = models.DateTimeField('дата обновления конфига', blank=True)