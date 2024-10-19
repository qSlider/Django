'''from django.test import TestCase
from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Post
from .models import Author
from .forms import PostForm


class AddPostViewTest(TestCase):
    def test_post(self):
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls2/add_post2.html')

    def test_add_post_view(self):
        data = {
            'title': 'New post',
            'content': 'Test content',
        }
        response = self.client.post(reverse('add_post'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)
        new_post = Post.objects.first()
        self.assertEqual(new_post.title, 'New post')
        self.assertEqual(new_post.content, 'Test content')'''