# Generated by Django 3.1.5 on 2021-01-29 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20210128_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='national',
            name='hospitalizedIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='national',
            name='negativeIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='national',
            name='positiveIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='national',
            name='states',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='national',
            name='totalTestResultIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='national',
            name='totalTestResults',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='dataQualityGrade',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='deathConfirmed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='deathIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='deathProbable',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='hospitalized',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='hospitalizedIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='negativeIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='negativeTestsAntibody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='negativeTestsPeopleAntibody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='negativeTestsViral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveCasesViral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveTestsAntibody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveTestsAntigen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveTestsPeopleAntibody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveTestsPeopleAntigen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='positiveTestsViral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='recovered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestEncountersViral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestEncountersViralIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestResults',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestResultsIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsAntibody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsAntigen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsPeopleAntibody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsPeopleAntigen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsPeopleViral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsPeopleViralIncrease',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsVira',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='totalTestsViralIncrease',
            field=models.IntegerField(default=0),
        ),
    ]
