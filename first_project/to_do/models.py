from django.db import models
from helpers.choices import STATUS_CHOICES


class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title