# Generated by Django 4.2.3 on 2023-07-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]