# Generated by Django 4.2.16 on 2024-11-13 13:44

import books.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, default='No description'),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default=books.models.get_default_cover, upload_to='covers/'),
        ),
    ]