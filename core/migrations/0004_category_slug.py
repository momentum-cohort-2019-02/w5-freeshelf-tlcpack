# Generated by Django 2.1.7 on 2019-03-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_add_books_again'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
