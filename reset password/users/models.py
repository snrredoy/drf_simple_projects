from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    attempt = models.IntegerField(default=0)
    is_varified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.created_at + timedelta(minutes=10) > now()