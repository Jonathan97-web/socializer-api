from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    friend = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friend')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['friend', 'user']
    
    def __str__(self):
        return f'{self.user} {self.friend}'