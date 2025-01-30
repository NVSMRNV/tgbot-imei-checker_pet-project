from pyexpat import model
from django.db import models
from django.db.models.fields import related


class WhiteList(models.Model):
    uid = models.PositiveBigIntegerField(
        verbose_name='Телеграм ID пользователя',
        unique=True,
        primary_key=True,
    )

    class Meta:
        db_table = 'whitelist'

    def __str__(self):
        return f'{self.uid}'
