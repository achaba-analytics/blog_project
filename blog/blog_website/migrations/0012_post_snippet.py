# Generated by Django 3.2.25 on 2025-06-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_website', '0011_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Read More', max_length=255),
        ),
    ]
