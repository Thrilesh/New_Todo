from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
