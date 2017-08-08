from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': _('Текст сообщения')})
        }