from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Post Model
class Post(models.Model):
    """A class that defines the post."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.title} by {self.author}"

# Comment Model
class Comment(models.Model):
    """A class that defines models."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.user.username
