# Generated by Django 3.1.5 on 2021-01-27 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20210127_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='national',
            old_name='inIcuCumulative',
            new_name='InIcuCumulative',
        ),
        migrations.RenameField(
            model_name='national',
            old_name='inIcuCurrently',
            new_name='InIcuCurrently',
        ),
    ]
