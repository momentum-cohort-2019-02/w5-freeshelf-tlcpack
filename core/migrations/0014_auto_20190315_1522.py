# Generated by Django 2.1.7 on 2019-03-15 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='book',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
