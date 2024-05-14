from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
