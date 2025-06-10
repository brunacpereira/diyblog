from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    """Model representing a post of blog """

    title = models.CharField(max_length=200)

    # Foreign Key used because post can only have one blogger, but blogger can have multiple blogs
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000, help_text='Enter a description of the post')
    
    date_of_post = models.DateField(null=True, blank=True)
 
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])


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


class Comment(models.Model):
    """Model representing an comment."""

    description = models.TextField(max_length=1000, help_text='Enter a comment about the post')
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True)
