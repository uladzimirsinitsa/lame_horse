# Generated by Django 2.2.5 on 2020-07-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_en', '0004_auto_20200719_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsen',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
