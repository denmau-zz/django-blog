# We use reverse_lazy as opposed to just reverse so that it won’t execute the URL redirect
# until our view has finished deleting the blog post.
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Post, Comment


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    # Only logged in user is allowed to edit post
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    # Only logged in user is allowed to delete post
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# A logged in user may add a new comment from the post_detail page
# The comment is captured in a form and sent to this view(mapped from url) using POST method
# This view is responsible for reading the POST details and creating a new Comment object from Comment model
# after this it returns the template that contains details about the post
# which is similar to refreshing the page, and thus the new comment is now visible


class CreateComment(View):
    def post(self, request, pk):
        received_comment = request.POST['comment']
        received_pk = Post.objects.get(id=pk)
        # instantiate new comment
        Comment.objects.create(comment=request.POST['comment'], post=Post(pk), author=auth.get_user(request))

        # print(f"Here is the PK: {received_pk}; and the request is {received_comment}")
        # return render(request, 'test.html', {'my_message': f"PK:{received_pk} : Message:{received_comment}"})
        return redirect('post_detail', pk)
        # Display POST parameters - for testing purposes
        # return render(request, 'test.html', {
        #     'my_message': {request.POST['comment']},
        # })
        # go back to post details
