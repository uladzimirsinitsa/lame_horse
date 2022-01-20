# Generated by Django 2.2.5 on 2020-01-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('message', models.TextField(max_length=1500, verbose_name='Message')),
            ],
        ),
    ]
