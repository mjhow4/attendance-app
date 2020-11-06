from django import forms
from .models import Contact, Note, Case


class Atten(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'file number',
            'defendant name',
            'complaint',
            'attourney',
            'cont',
            
        ]

class NoteForm(forms.ModelForm): 
    class Meta: 
        model = Note
        fields = [
            'txt'
        ]
