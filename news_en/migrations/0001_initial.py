# Generated by Django 2.2.5 on 2020-06-29 12:46

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TagNewsEn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тег')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='NewsEn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80)),
                ('keywords', models.CharField(blank=True, default='#', max_length=600)),
                ('slug', models.SlugField(default=uuid.uuid4, max_length=80, unique=True, verbose_name='Слаг')),
                ('imgcloud', models.CharField(blank=True, default='#', max_length=300)),
                ('imagealtcloud', models.CharField(blank=True, default='#', max_length=80)),
                ('img78', models.CharField(blank=True, default='#', max_length=300)),
                ('imagealt78', models.CharField(blank=True, default='#', max_length=80)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('description', models.TextField(max_length=160)),
                ('localization_en', models.CharField(blank=True, default='#', max_length=100)),
                ('urlaff', models.CharField(blank=True, default='#', max_length=300)),
                ('review', models.CharField(blank=True, default='#', max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='promo', to='news_en.TagNewsEn', verbose_name='Теги')),
            ],
            options={
                'ordering': ['-date_update'],
            },
        ),
    ]
