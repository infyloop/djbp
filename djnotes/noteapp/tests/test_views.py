from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django_dynamic_fixture import G
import json
from urllib import urlencode

from noteapp.models import Note

class TestNoteListView(TestCase):

    """ Test for the contacts list view """

    def setUp(self):
        self.note = G(Note)
        
    def test_list_view(self):
        url = reverse('notes-list')
        response = self.client.get(url)
        # test for the status code
        self.assertEquals(response.status_code, 200)
        # test for context variable
        self.assertTrue('note_list' in response.context)
        # test for the count of the context variable
        self.assertEquals(response.context['object_list'].count(), 1)
        # test for the value of the context variable
        note_zero = response.context['note_list'][0]
        self.assertEquals(note_zero.title, self.note.title)
        self.assertEquals(note_zero.description, self.note.description)
        # test the template used
        self.assertTemplateUsed(response, 'note_list.html')

    def test_create_view(self):

        url = reverse("notes-create")
        post = {"title": "title", "description": "some desc"}
        response = self.client.post(url, post)
        self.assertEquals(response.status_code, 302)
        

    def test_note_view(self):
        
        url = reverse('notes-view', kwargs={'pk': self.note.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'note.html')
        # test for the value of the context variable
        self.assertEquals(response.context_data['note'], self.note)

        
    def test_delete_note_view(self):
        url = reverse('notes-delete', kwargs={'pk':self.note.id})
        response = self.client.delete(url)
        self.assertEquals(Note.objects.count(), 0)
        self.assertEquals(response.status_code, 302)


    def test_update_note_view(self):
        url = reverse('notes-edit', kwargs={'pk':self.note.id})
        post = {"title": "Hello", "description": "World"}
        response = self.client.post(url, post)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Note.objects.get(pk=self.note.id).title, "Hello")
        self.assertEquals(Note.objects.get(pk=self.note.id).description, "World")
    
