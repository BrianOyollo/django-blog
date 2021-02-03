from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True, max_length=500)

    def __str__(self):
        return f'{self.user.username} is {self.about}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
