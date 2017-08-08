from channels.routing import route
from channels import Group, Channel
from channels.auth import channel_session_user_from_http, channel_session_user

import json

from .forms import MessageForm

@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({'accept': True})
    Group('chat').add(message.reply_channel)


@channel_session_user
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)


@channel_session_user
def ws_receive(message):
    Channel('chat_send').send(
        {
            'text':message['text'],
            'reply_channel':message.content['reply_channel']
        })


@channel_session_user
def chat_send(message):

    data = json.loads(message['text'])
    form = MessageForm(data)
    if form.is_valid():
        msg = form.save(commit=False)
        msg.owner = message.user
        msg.save()
        data = {
            'text': msg.text, 'owner': msg.owner.username,
            'when_created': str(msg.when_created.strftime('%d-%m-%Y %H:%M'))
        }

        Group('chat').send({'text': json.dumps(data)})
    else:
        message.reply_channel.send(
            {'text': json.dumps({'errors': form.errors.as_json()})}
        )


channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),  # we register our message handler
    route('websocket.disconnect', ws_disconnect),
    route('chat_send', chat_send)
]