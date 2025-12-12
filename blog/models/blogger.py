from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth import get_user_model

class Blogger(models.Model):
    """Model representing an blogger."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, help_text='Enter a bio of the blogger')
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['first_name','last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'