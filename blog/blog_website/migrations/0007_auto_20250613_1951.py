# Generated by Django 3.2.25 on 2025-06-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_website', '0006_auto_20250613_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
