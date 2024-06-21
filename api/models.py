from django.db import models
from users.models import User

class Status(models.TextChoices):
    NEW = "NEW", "Nowy"
    IN_PROGRESS = "IN_PROGRESS", "W toku"
    RESOLVED = "RESOLVED", "Rozwiązany"
    DELETED = "DELETED", "Usunięte"

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="Brak opisu")
    assignedUser = models.ForeignKey(User, related_name="user", null=True, blank=True, on_delete=models.CASCADE, to_field='email')
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.NEW
    )

class BackLog(models.Model):
    id = models.AutoField(primary_key=True)
    task_data = models.JSONField(default=dict)
    modification_date = models.DateTimeField(auto_now=True)

    @classmethod
    def set_backlog_data(cls, task):

        task_data = {
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'assignedUser': task.assignedUser.email if task.assignedUser else None,
            'status': task.status,
        }
        backlog = cls(task_data=task_data)
        backlog.save()
        return backlog
