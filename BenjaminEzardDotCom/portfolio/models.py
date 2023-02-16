from django.db import models

class Article(models.Model):
    articleId = models.PositiveBigIntegerField(primary_key=True)
    isActive = models.BooleanField(default=True)
    isPublished = models.BooleanField(default=False)
    name = models.CharField(max_length=256, unique=True)
    title = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=4096)
    githubLink = models.CharField(max_length=4096)