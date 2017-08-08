from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Message
from .forms import MessageForm
# Create your views here.


class ChatView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'chat/chat.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = MessageForm()
        return data