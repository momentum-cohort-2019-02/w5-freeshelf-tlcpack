from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=250)

    author = models.CharField(max_length=250)

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, help_text='For which language is this book?')

    #URL field, need to add way to ensure unique URL
    url = models.URLField(max_length=250)

    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Category(models.Model):
    language = models.CharField(max_length=100)

    # slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        return self.language