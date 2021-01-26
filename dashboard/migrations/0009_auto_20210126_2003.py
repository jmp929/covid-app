# Generated by Django 3.1.5 on 2021-01-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210125_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='national',
            name='InIcuCumulative',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='InIcuCurrently',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='date',
            field=models.DateField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='national',
            name='death',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='deathIncrease',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='hospitalizedCumulative',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='hospitalizedCurrently',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='hospitalizedIncrease',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='negative',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='negativeIncrease',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='onVentilatorCumulative',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='onVentilatorCurrently',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='positive',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='positiveIncrease',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='states',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='totalTestResults',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='national',
            name='totalTestResultsIncrease',
            field=models.IntegerField(default=0, max_length=11),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together={('state', 'date')},
        ),
    ]
