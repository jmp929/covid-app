# Generated by Django 3.1.5 on 2021-01-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210124_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='national',
            name='date',
            field=models.TextField(),
        ),
    ]
