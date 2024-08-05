from django import forms
from django.db import models
from models.project import Project


class Status(models.TextChoices):
    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Closed"
    STARTED = "STARTED", "Started"
    BACKLOG = "BACKLOG", "Backlog"


class Role(models.TextChoices):
    BACKEND = "BACKEND", "Backend"
    FRONTEND = "FRONTEND", "Frontend"
    FULLSTCK = "FULLSTCK", "Fullstck"
    QA = "QA", "QA"
    DESIGN = "DESIGN", "Design"
    PM = "PM", "PM"
    DEVOPS = "DEVOPS", "Devops"
    OTHER = "OTHER", "Other"

class ProjectCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.Textarea()
    repo_link = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=Status)
    author_role = forms.ChoiceField(choices=Role)
    deadline = forms.DateTimeField(required=False)

    class Meta:
        model = Project
        fields = ['name', 'description', 'repo_link', 'status', 'author_role', 'deadline']