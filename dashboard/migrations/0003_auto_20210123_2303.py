# Generated by Django 3.1.5 on 2021-01-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210123_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='national',
            name='date',
            field=models.CharField(default='', max_length=11),
        ),
    ]