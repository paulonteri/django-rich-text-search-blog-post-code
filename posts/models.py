from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"Title: `{self.title}` | Description: `{self.description}`"


