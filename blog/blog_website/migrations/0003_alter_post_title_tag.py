# Generated by Django 3.2.25 on 2025-06-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_website', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My blog', max_length=255),
        ),
    ]
