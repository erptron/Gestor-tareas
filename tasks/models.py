from django.db import models
from ckeditor.fields import RichTextField

class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class ProjectType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class TaskType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, related_name='project_state', on_delete=models.RESTRICT)  # ForeignKey
    type = models.ForeignKey(ProjectType, related_name='project_type', on_delete=models.RESTRICT)  # ForeignKey
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    assignee = models.ForeignKey(User, related_name='asignee', on_delete=models.RESTRICT, null=True, blank=True)  # ForeignKey
    state = models.ForeignKey(State, related_name='state', on_delete=models.RESTRICT, null=True)  # ForeignKey
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.RESTRICT)  # ForeignKey
    priority = models.ForeignKey(Priority, related_name='tasks', on_delete=models.RESTRICT)  # ForeignKey
    parent = models.ForeignKey('self', related_name='subtasks', on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"

class Comment(models.Model):
    description = RichTextField(blank=True)
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.RESTRICT, null=True, blank=True)  # ForeignKey
    project = models.ForeignKey(Project, related_name='comment_project', on_delete=models.RESTRICT, null=True, blank=True)  # ForeignKey
    task = models.ForeignKey(Task, related_name='comment_task', on_delete=models.RESTRICT, null=True, blank=True)  # ForeignKey
    parent = models.ForeignKey('self', related_name='comment_parent', on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"
