# forms.py
from django import forms
from .models import Task, Project
from ckeditor.widgets import CKEditorWidget

imput_syle = {
    'class': 'form-control',
    'style': 'width: 100%; box-sizing: border-box;'
}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'state', 'project', 'parent']
        widgets = {
            'title': forms.TextInput(attrs=imput_syle),
            'description': CKEditorWidget(),
            'assignee': forms.Select(attrs=imput_syle),
            'state': forms.Select(attrs=imput_syle),
            'project': forms.Select(attrs=imput_syle),
            'parent': forms.Select(attrs=imput_syle),
        }

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'state', 'project', 'parent']
        widgets = {
            'title': forms.TextInput(attrs=imput_syle),
            'description': CKEditorWidget(),
            'assignee': forms.Select(attrs=imput_syle),
            'state': forms.Select(attrs=imput_syle),
            'project': forms.Select(attrs=imput_syle),
            'parent': forms.Select(attrs=imput_syle),
        }


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'state', 'project']
        widgets = {
            'title': forms.TextInput(attrs=imput_syle),
            'description': CKEditorWidget(),
            'assignee': forms.Select(attrs=imput_syle),
            'state': forms.Select(attrs=imput_syle),
            'project': forms.Select(attrs=imput_syle),
        }

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'state', 'project']
        widgets = {
            'title': forms.TextInput(attrs=imput_syle),
            'description': CKEditorWidget(),
            'assignee': forms.Select(attrs=imput_syle),
            'state': forms.Select(attrs=imput_syle),
            'project': forms.Select(attrs=imput_syle),
        }

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'state', 'description']
        widgets = {
            'title': forms.TextInput(attrs=imput_syle),
            'state': forms.Select(attrs=imput_syle),
            'description': CKEditorWidget(),
        }

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'state', 'type', 'description']
        widgets = {
            'title': forms.TextInput(attrs=imput_syle),
            'state': forms.Select(attrs=imput_syle),
            'type': forms.Select(attrs=imput_syle),
            'description': CKEditorWidget(attrs=imput_syle)
        }