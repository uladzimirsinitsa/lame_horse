# Generated by Django 2.2.5 on 2020-11-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_en', '0010_auto_20200409_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_en',
            name='example',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='article_en',
            name='title',
            field=models.CharField(db_index=True, max_length=70),
        ),
    ]
