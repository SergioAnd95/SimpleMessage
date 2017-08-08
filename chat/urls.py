from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.ChatView.as_view(), name='chat')
]