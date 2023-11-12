from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    CATEGORY_CHOICES = (
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('biography', 'Biography'),
        ('self-help', 'Self-Help'),
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)
    published = models.DateField()
    iso = models.CharField(max_length=10)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BlogPostSubscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

