from django import forms
from .models import Contact, Note, Case


class Case(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'file number',
            'Attorney',
            'court date',
            'court session',
            'plea request',
            
        ]

class Attorney(forms.ModelForm):
    class Meta:
        model = Attorney
        fields = [
            'Attorney name',
            'Forgien Key to user',
            
            
        ]

class Plea(forms.ModelForm):
    class Meta:
        model = Plea
        fields = [
            'date requested',
            'Accepted or not',
            
        ]

class User(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'file number',
            'Attorney',
            'court date',
            'court session',
            'plea request',
            
        ]


class NoteForm(forms.ModelForm): 
    class Meta: 
        model = Note
        fields = [
            'txt'
        ]
