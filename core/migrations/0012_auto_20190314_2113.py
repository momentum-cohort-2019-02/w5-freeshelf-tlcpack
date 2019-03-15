# Generated by Django 2.1.7 on 2019-03-15 01:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190314_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_books', to=settings.AUTH_USER_MODEL),
        ),
    ]