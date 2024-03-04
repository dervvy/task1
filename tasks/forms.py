from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Task
from django.forms import DateInput

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class TaskForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    deadline = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'completed', 'priority']
        widgets = {
            'deadline': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }