from django.test import TestCase
from .models import Entry

# Create your tests here.



class EntryModelTest():
    def test_string_representation(self):
     entry = Entry(title="My entry title")
     self.assertEqual(str(entry), entry.title)

