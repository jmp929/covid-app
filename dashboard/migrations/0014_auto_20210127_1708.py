# Generated by Django 3.1.5 on 2021-01-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20210127_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.TextField(max_length=2),
        ),
    ]
