# Generated by Django 3.1.5 on 2021-01-27 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20210127_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='national',
            old_name='InIcuCumulative',
            new_name='inIcuCumulative',
        ),
        migrations.RenameField(
            model_name='national',
            old_name='InIcuCurrently',
            new_name='inIcuCurrently',
        ),
    ]