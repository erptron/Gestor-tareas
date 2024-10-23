from django.db import models
from ckeditor.fields import RichTextField

class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    state = models.ForeignKey(State, related_name='project_state', on_delete=models.RESTRICT, null=True)  # ForeignKey

    def __str__(self):
        return f"{self.title}"

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    asignee = models.ForeignKey(User, related_name='asignee', on_delete=models.RESTRICT, null=True)  # ForeignKey
    state = models.ForeignKey(State, related_name='state', on_delete=models.RESTRICT, null=True)  # ForeignKey
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.RESTRICT)  # ForeignKey
    parent = models.ForeignKey('self', related_name='subtasks', on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey a sí mismo

    def __str__(self):
        return f"{self.description}"
