# Generated by Django 2.2.5 on 2020-06-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino_online_en', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino_en',
            name='imgcloudsearch',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
    ]