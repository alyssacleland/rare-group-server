from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=100, default=True)

    def __str__(self):
        return self.label
