from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Chat


class ChatTests(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.chat = None

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Chat.objects.create(
            message='Nice message content',
            sender=self.user,
        )

    def test_string_representation(self):
        sample_chat = Chat(message='A sample message')

        self.assertEqual(str(sample_chat), sample_chat.message)

    def test_chat_content(self):
        self.assertEqual(f'{self.chat.message}', 'Nice message content')
        self.assertEqual(f'{self.chat.sender}', 'testuser')

    def test_chat_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice message content')
        self.assertTemplateUsed(response, 'home.html')

    def test_chat_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'message': 'Test text',
            'sender': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Chat.objects.last().message, 'Test text')
