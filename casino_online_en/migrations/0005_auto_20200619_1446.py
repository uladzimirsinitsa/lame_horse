# Generated by Django 2.2.5 on 2020-06-19 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casino_online_en', '0004_auto_20200614_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casino_en',
            old_name='activate',
            new_name='published',
        ),
    ]
