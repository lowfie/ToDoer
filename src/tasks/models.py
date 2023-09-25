from datetime import datetime

from django.db import models

from src.users.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=1024)
    due_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def due_date_timestamp(self) -> int:
        return int(self.due_date.timestamp())

    @due_date_timestamp.setter
    def due_date_timestamp(self, value) -> None:
        self.due_date = datetime.fromtimestamp(int(value))
