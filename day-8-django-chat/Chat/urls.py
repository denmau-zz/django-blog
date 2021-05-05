from django.urls import path

from .views import ChatListView, ChatCreateView

urlpatterns = [
    path('chat/new/', ChatCreateView.as_view(), name='post_new'),
    path('', ChatListView.as_view(), name='home'),
]
