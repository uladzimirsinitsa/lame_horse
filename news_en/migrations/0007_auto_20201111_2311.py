# Generated by Django 2.2.5 on 2020-11-11 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_en', '0006_newsen_users_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsen',
            options={'ordering': ['-date']},
        ),
    ]
