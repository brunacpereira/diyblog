from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth import get_user_model

class Comment(models.Model):
    """Model representing an comment."""

    description = models.TextField(max_length=1000, help_text='Enter a comment about the post')
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True)