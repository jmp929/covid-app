# Generated by Django 3.1.5 on 2021-01-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20210127_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
