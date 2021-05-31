from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',  # will use this for relationship backward
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])
