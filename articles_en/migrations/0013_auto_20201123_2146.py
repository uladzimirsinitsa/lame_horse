# Generated by Django 2.2.5 on 2020-11-23 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles_en', '0012_auto_20201119_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_en',
            name='example',
        ),
        migrations.RemoveField(
            model_name='article_en',
            name='imagealt78',
        ),
        migrations.RemoveField(
            model_name='article_en',
            name='img78',
        ),
    ]
