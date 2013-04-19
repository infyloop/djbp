from django.test import TestCase
from django_dynamic_fixture import G

from noteapp.models import Note 

class NoteModelTest(TestCase):

    def test_note_creation(self):
        ''' Test the creation and saving of a new note '''
        note1 = G(Note)
        note2 = G(Note)
        notes_in_db = Note.objects.all()
        self.assertEquals(notes_in_db.count(), 2)
        
        # check the values stored 
        note_zero = notes_in_db[0] 
        self.assertEquals(note_zero.title, note1.title) 
        self.assertEquals(note_zero.description, note1.description)
        self.assertEquals(note_zero.pub_date, note1.pub_date)
