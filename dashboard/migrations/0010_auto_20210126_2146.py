# Generated by Django 3.1.5 on 2021-01-26 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210126_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='national',
            name='deathIncrease',
        ),
        migrations.RemoveField(
            model_name='national',
            name='hospitalizedIncrease',
        ),
        migrations.RemoveField(
            model_name='national',
            name='negativeIncrease',
        ),
        migrations.RemoveField(
            model_name='national',
            name='positiveIncrease',
        ),
        migrations.RemoveField(
            model_name='national',
            name='states',
        ),
        migrations.RemoveField(
            model_name='national',
            name='totalTestResults',
        ),
        migrations.RemoveField(
            model_name='national',
            name='totalTestResultsIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='dataQualityGrade',
        ),
        migrations.RemoveField(
            model_name='state',
            name='deathConfirmed',
        ),
        migrations.RemoveField(
            model_name='state',
            name='deathIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='deathProbable',
        ),
        migrations.RemoveField(
            model_name='state',
            name='hospitalized',
        ),
        migrations.RemoveField(
            model_name='state',
            name='hospitalizedIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='negativeIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='negativeTestsAntibody',
        ),
        migrations.RemoveField(
            model_name='state',
            name='negativeTestsPeopleAntibody',
        ),
        migrations.RemoveField(
            model_name='state',
            name='negativeTestsViral',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveCasesViral',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveScore',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveTestsAntibody',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveTestsAntigen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveTestsPeopleAntibody',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveTestsPeopleAntigen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='positiveTestsViral',
        ),
        migrations.RemoveField(
            model_name='state',
            name='recovered',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestEncountersViral',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestEncountersViralIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestResults',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestResultsIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsAntibody',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsAntigen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsPeopleAntibody',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsPeopleAntigen',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsPeopleViral',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsPeopleViralIncrease',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsViral',
        ),
        migrations.RemoveField(
            model_name='state',
            name='totalTestsViralIncrease',
        ),
    ]
