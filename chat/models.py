from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Message(models.Model):
    text = models.TextField(_('Текст'))
    owner = models.ForeignKey(
        User,
        verbose_name=_('Владелец'),
        related_name='messages'
    )

    when_created = models.DateTimeField(_('Когда создан?'), auto_now_add=True)