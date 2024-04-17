from django.db import models
from cours.models import Mentor
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField()
    image = models.ImageField(upload_to='media/blog/blog')
    author = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
