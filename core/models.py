from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=250)

    author = models.CharField(max_length=250)

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, help_text='For which language is this book?')

    #URL field, need to add way to ensure unique URL
    url = models.URLField(max_length=250)

    date = models.DateField(auto_now_add=True)

    favorited_by = models.ManyToManyField(to=User, related_name='favorite_books')


    # making slug
    slug = models.SlugField(null=True, blank=True)

    def get_slug(self):
        if self.slug:
            return
        self.slug = slugify(self.title)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Category(models.Model):
    """Model for programming languages"""
    language = models.CharField(max_length=100)

    # making slug
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.set_slug()
    #     super().save(*args, **kwargs)

    # def set_slug(self):
    #     if self.slug:
    #         return

    #     base_slug = slugify(self.title)
    #     slug = base_slug
    #     n = 0

    #     while Category.objects.filter(slug=slug).count():
    #         n += 1
    #         slug = base_slug + "-" + str(n)

    #     self.slug = slug

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        return self.language


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)