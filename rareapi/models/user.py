from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=400)
    profile_image_url = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    created_on = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    uid = models.CharField(max_length=60)