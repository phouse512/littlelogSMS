from django.db import models
from django.utils import timezone

# Create your models here.


class LittleLogAlias(models.Model):
    id = models.AutoField(primary_key=True)
    alias = models.CharField(max_length=20)
    email_secret = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)


class LittleLogHistory(models.Model):
    id = models.AutoField(primary_key=True)
    sent_time = models.DateTimeField(default=timezone.now)
    alias = models.ForeignKey(LittleLogAlias)
    log_text = models.CharField(max_length=255)


