from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']  # Fields required on createsuperuser

    def __str__(self):
        return
