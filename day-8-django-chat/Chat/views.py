# We use reverse_lazy as opposed to just reverse so that it won’t execute the URL redirect
# until our view has finished deleting the Chat post.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from Chat.models import Chat


class ChatListView(ListView):
    model = Chat
    template_name = 'home.html'


class ChatCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Chat
    template_name = 'chat_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
