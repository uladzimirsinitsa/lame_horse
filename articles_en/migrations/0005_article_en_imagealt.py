# Generated by Django 2.2.5 on 2020-02-08 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_en', '0004_auto_20200119_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_en',
            name='imagealt',
            field=models.CharField(blank=True, default='#', max_length=80),
        ),
    ]
