from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author} - {self.title}"

