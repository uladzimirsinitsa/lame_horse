# Generated by Django 2.2.5 on 2020-11-23 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles_en', '0013_auto_20201123_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_en',
            name='imagealt',
        ),
        migrations.RemoveField(
            model_name='article_en',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag_en',
        ),
    ]