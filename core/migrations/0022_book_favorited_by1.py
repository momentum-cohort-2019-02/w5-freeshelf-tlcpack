# Generated by Django 2.1.7 on 2019-03-16 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0021_auto_20190316_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_by1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorited_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
