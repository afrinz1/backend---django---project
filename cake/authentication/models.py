from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    USER = "user","user"
    ADMIN = "admin","admin"

class Profile(AbstractUser):

    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    def __str__(self):

        return self.username

    class Meta:

        verbose_name_plural = "categories"