from django.urls import path

from .views import ChatListView, ChatCreateView, process_chat

urlpatterns = [
    # path('chat_new/', ChatCreateView.as_view(), name='chat_new'),
    path('new_chat/', process_chat),
    path('', ChatListView.as_view(), name='home'),
]
