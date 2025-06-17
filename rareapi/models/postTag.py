from django.db import models
from .post import Post
from .tag import Tag 

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post_tags')

    def __str__(self):
        return f"{self.post.title} - {self.tag.label}"
