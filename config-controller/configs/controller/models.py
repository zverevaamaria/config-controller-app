from django.db import models
from django.utils import timezone
import datetime

class Config(models.Model):
    service = models.CharField('сервис конфига', max_length=200, unique=True,  blank=True)
    data = models.JSONField('содержимое конфига')
    version = models.IntegerField('версия конфига')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField('дата создания конфига',  default=timezone.now)
    updated_at = models.DateTimeField('дата обновления конфига', blank=True)