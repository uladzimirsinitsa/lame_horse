# Generated by Django 2.2.5 on 2020-07-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo_en', '0003_auto_20200708_2201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promoen',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='promoen',
            name='over',
            field=models.CharField(blank=True, default='#', max_length=10),
        ),
    ]
