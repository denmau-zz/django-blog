# We use reverse_lazy as opposed to just reverse so that it won’t execute the URL redirect
# until our view has finished deleting the Chat post.
from abc import ABC

from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from Chat.models import Chat


class ChatListView(ListView):
    model = Chat
    template_name = 'home.html'


class ChatCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView, ABC):
    model = Chat
    template_name = 'chat_new.html'
    fields = ['message']

    # ensure that message has been sent by currently logged-in user
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


# I found that using a function here as opposed to a class is a lot easier
def process_chat(request):
    # create instances of chat
    # model = Chat
    Chat.objects.create(message=request.POST['chat'], sender=auth.get_user(request))
    # Chat(message=request.POST['chat'], sender=auth.get_user(request))
    return render(request, 'home.html', {
        'post_data': f"Chat Message: {request.POST['chat']}",
        'post_data_type': f"Current User: {auth.get_user(request)}",
    })
