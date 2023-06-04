from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'due_date', 'tags']
