# Generated by Django 2.2.5 on 2020-06-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino_online_en', '0005_auto_20200619_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casino_en',
            name='template',
        ),
        migrations.RemoveField(
            model_name='casino_en',
            name='thumbnail_600x250',
        ),
        migrations.AddField(
            model_name='casino_en',
            name='alt_logo',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='alternate_en',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='alternate_ru',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='canonical',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='logo834100',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='title_meta',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='url_affilate',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='casino_en',
            name='youtube',
            field=models.CharField(blank=True, default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='casino_en',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='casino_en',
            name='keywords',
            field=models.CharField(max_length=500, verbose_name='???????????????? ??????????'),
        ),
    ]
