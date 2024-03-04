from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.title