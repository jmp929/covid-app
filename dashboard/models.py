from django.db import models
from django.urls import reverse
import django_tables2 as tables

class National(models.Model):
			date = models.DateField(unique=True, max_length=11)
			death = models.IntegerField(default=0, max_length=11)
			deathIncrease = models.IntegerField(default=0, max_length=11)
			InIcuCumulative = models.IntegerField(default=0, max_length=11)
			InIcuCurrently = models.IntegerField(default=0, max_length=11)
			hospitalizedIncrease = models.IntegerField(default=0, max_length=11)
			hospitalizedCurrently = models.IntegerField(default=0, max_length=11)
			hospitalizedCumulative = models.IntegerField(default=0, max_length=11)
			negative = models.IntegerField(default=0, max_length=11)
			negativeIncrease = models.IntegerField(default=0, max_length=11)
			onVentilatorCumulative = models.IntegerField(default=0, max_length=11)
			onVentilatorCurrently = models.IntegerField(default=0, max_length=11)
			positive = models.IntegerField(default=0, max_length=11)
			positiveIncrease = models.IntegerField(default=0, max_length=11)
			states = models.IntegerField(default=0, max_length=11)
			totalTestResults = models.IntegerField(default=0, max_length=11)
			totalTestResultsIncrease = models.IntegerField(default=0, max_length=11)

			

			def get_absolute_url(self):
				return reverse("national-detail", kwargs={"id": self.id})

			def __str__(self):
				return "date: " + str(self.date) + "and number of deaths: " + str(self.id)

# class NationalTable(tables.Table):
# 	class Meta:
# 		model = National




class State(models.Model):
			date = models.DateField()
			state = models.TextField()
			dataQualityGrade = models.TextField()
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

			class Meta:
				unique_together = ['state', 'date']



# class StateTable(tables.Table):
# 	class Meta:
# 		model = State















			
