from django.db import models
from .user import User
from .category import Category
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
