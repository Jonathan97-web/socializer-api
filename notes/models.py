from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Notes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    notes = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id}, {self.notes}, {self.owner}"
