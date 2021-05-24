from django.db import models

class Todo(models.Model):
    title = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.title}"

