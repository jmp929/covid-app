from django.db import models
from django.urls import reverse
import django_tables2 as tables

class National(models.Model):
	date = models.DateField(max_length=11)
	death = models.IntegerField(default=0)
	deathIncrease = models.IntegerField(default=0)
	InIcuCumulative = models.IntegerField(default=0)
	InIcuCurrently = models.IntegerField(default=0)
	hospitalizedIncrease = models.IntegerField(default=0)
	hospitalizedCurrently = models.IntegerField(default=0)
	hospitalizedCumulative = models.IntegerField(default=0)
	negative = models.IntegerField(default=0)
	negativeIncrease = models.IntegerField(default=0)
	onVentilatorCumulative = models.IntegerField(default=0)
	onVentilatorCurrently = models.IntegerField(default=0)
	positive = models.IntegerField(default=0)
	positiveIncrease = models.IntegerField(default=0)
	states = models.IntegerField(default=0)
	totalTestResults = models.IntegerField(default=0)
	totalTestResultIncrease = models.IntegerField(default=0)

	@classmethod
	def get_expected_names(clas):
		return ['date', 'death', 'deathIncrease', 'InIcuCumulative', 'InIcuCurrently', 'hospitalizedIncrease', 'hospitalizedCurrently', 'hospitalizedCumulative', 'negative', 'negativeIncrease', 'onVentilatorCumulative',
				'onVentilatorCurrently', 'positive', 'positiveIncrease', 'states', 'totalTestResults', 'totalTestResultsIncrease']

	def get_date(self):
		return self.date

	def get_death(self):
		return self.deathIncrease


			


# class NationalTable(tables.Table):
# 	class Meta:
# 		model = National




class State(models.Model):
	date = models.DateField()
	state = models.CharField(max_length=2)
	dataQualityGrade = models.CharField(max_length=2)
	death = models.IntegerField(default=0)
	deathConfirmed = models.IntegerField(default=0)
	deathIncrease = models.IntegerField(default=0)
	deathProbable = models.IntegerField(default=0)
	hospitalized = models.IntegerField(default=0)
	hospitalizedCumulative = models.IntegerField(default=0)
	hospitalizedCurrently = models.IntegerField(default=0)
	hospitalizedIncrease = models.IntegerField(default=0)
	inIcuCumulative = models.IntegerField(default=0)
	inIcuCurrently = models.IntegerField(default=0)
	negative = models.IntegerField(default=0)
	negativeIncrease = models.IntegerField(default=0)
	negativeTestsAntibody = models.IntegerField(default=0)
	negativeTestsPeopleAntibody = models.IntegerField(default=0)
	negativeTestsViral = models.IntegerField(default=0)	
	onVentilatorCumulative = models.IntegerField(default=0)
	onVentilatorCurrently = models.IntegerField(default=0)
	positive = models.IntegerField(default=0)
	positiveCasesViral = models.IntegerField(default=0)	
	positiveIncrease = models.IntegerField(default=0)	
	positiveScore = models.IntegerField(default=0)	
	positiveTestsAntibody = models.IntegerField(default=0)	
	positiveTestsAntigen = models.IntegerField(default=0)	
	positiveTestsPeopleAntibody = models.IntegerField(default=0)	
	positiveTestsPeopleAntigen = models.IntegerField(default=0)	
	positiveTestsViral = models.IntegerField(default=0)	
	recovered = models.IntegerField(default=0)
	totalTestEncountersViral = models.IntegerField(default=0)	
	totalTestEncountersViralIncrease = models.IntegerField(default=0)	
	totalTestResults = models.IntegerField(default=0)	
	totalTestResultsIncrease = models.IntegerField(default=0)	
	totalTestsAntibody = models.IntegerField(default=0)	
	totalTestsAntigen = models.IntegerField(default=0)	
	totalTestsPeopleAntibody = models.IntegerField(default=0)	
	totalTestsPeopleAntigen = models.IntegerField(default=0)	
	totalTestsPeopleViral = models.IntegerField(default=0)	
	totalTestsPeopleViralIncrease = models.IntegerField(default=0)	
	totalTestsViral = models.IntegerField(default=0)	
	totalTestsViralIncrease = models.IntegerField(default=0)

	# class Meta:
	# 	unique_together = ['state', 'date']



	@classmethod
	def get_expected_names(clas):
		return ['date',
				'state',
				'dataQualityGrade',
				'death',
				'deathConfirmed',
				'deathIncrease',
				'deathProbable',
				'hospitalized',
				'hospitalizedCumulative',
				'hospitalizedCurrently',
				'hospitalizedIncrease',
				'inIcuCumulative',
				'inIcuCurrently',
				'negative',
				'negativeIncrease',
				'negativeTestsAntibody',
				'negativeTestsPeopleAntibody',
				'negativeTestsViral',
				'onVentilatorCumulative',
				'onVentilatorCurrently',
				'positive',
				'positiveCasesViral',
				'positiveIncrease',
				'positiveScore',
				'positiveTestsAntibody',
				'positiveTestsAntigen',
				'positiveTestsPeopleAntibody',
				'positiveTestsPeopleAntigen',
				'positiveTestsViral',
				'recovered',
				'totalTestEncountersViral',
				'totalTestEncountersViralIncrease',	
				'totalTestResults', 
				'totalTestResultsIncrease',
				'totalTestsAntibody',
				'totalTestsAntigen', 
				'totalTestsPeopleAntibody',
				'totalTestsPeopleAntigen',
				'totalTestsPeopleViral',
				'totalTestsPeopleViralIncrease',
				'totalTestsViral',
				'totalTestsViralIncrease'
				]



# class StateTable(tables.Table):
# 	class Meta:
# 		model = State















			
