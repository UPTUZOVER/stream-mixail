from django.db import models

class Project(models.Model):
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

    name = models.CharField(max_length=100)
    description = models.TextField()
    repo_link = models.CharField(max_length=100)
    status = models.CharField(choices=Status.choices, default=Status.OPEN,max_length=100)
    author_role = models.CharField(choices=Role.choices, default=Role.BACKEND,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="User_user")


    def __str__(self):
        return self.name




