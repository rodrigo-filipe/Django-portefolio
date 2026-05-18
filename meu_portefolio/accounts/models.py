from django.db import models
from django.contrib.auth.models import User
import uuid

class MagicToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def is_valid(self):
        from django.utils import timezone
        import datetime
        # Token valid for 15 minutes
        return not self.used and self.created_at > timezone.now() - datetime.timedelta(minutes=15)

    def __str__(self):
        return f"Token for {self.user.username}"
