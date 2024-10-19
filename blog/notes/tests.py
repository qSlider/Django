from django.test import TestCase
from django.utils import timezone
from .models import Note, Category
# notes/views.py
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , redirect
from django.urls import reverse, reverse_lazy
from .models import Post, Note, Author, Category
from .forms import PostForm , NoteForm



class NoteModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Тестова категорія")

    def test_create_note(self):
        note = Note.objects.create(
            title="Тестова нотатка",
            text="Це текст для тестової нотатки.",
            reminder=timezone.now(),
            category=self.category
        )

        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(note.title, "Тестова нотатка")
        self.assertEqual(note.text, "Це текст для тестової нотатки.")
        self.assertEqual(note.category.title, "Тестова категорія")

    def test_update_note(self):
        note = Note.objects.create(
            title="Тестова нотатка",
            text="Це текст для тестової нотатки.",
            reminder=timezone.now(),
            category=self.category
        )

        note.title = "Оновлена нотатка"
        note.text = "Це оновлений текст."
        note.save()

        updated_note = Note.objects.get(id=note.id)
        self.assertEqual(updated_note.title, "Оновлена нотатка")
        self.assertEqual(updated_note.text, "Це оновлений текст.")