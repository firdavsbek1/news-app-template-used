# Generated by Django 4.2.3 on 2023-07-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('D', 'Draft '), ('R', 'Ready ')], default='Draft', max_length=1),
        ),
    ]
