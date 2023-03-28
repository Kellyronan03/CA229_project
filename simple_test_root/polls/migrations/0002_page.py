# Generated by Django 3.2.12 on 2023-03-28 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('create_date', models.DateField(default=datetime.date.today, verbose_name='First Published')),
                ('bodytext', models.TextField(blank=True, verbose_name='Page Content')),
            ],
        ),
    ]
