from django.db import models
from django.urls import reverse
import django_tables2 as tables

class National(models.Model):
			date = models.DateField(unique=True, max_length=11)
			death = models.IntegerField(default=0)
			inIcuCumulative = models.IntegerField(default=0)
			inIcuCurrently = models.IntegerField(default=0)
			hospitalizedCurrently = models.IntegerField(default=0)
			hospitalizedCumulative = models.IntegerField(default=0)
			negative = models.IntegerField(default=0)
			onVentilatorCumulative = models.IntegerField(default=0)
			onVentilatorCurrently = models.IntegerField(default=0)
			positive = models.IntegerField(default=0)

			@classmethod
			def get_expected_names(clas):
				return ['date', 'death', 'InIcuCumulative','InIcuCurrently', 'hospitalizedCurrently', 'hospitalizedCumulative', 'negative', 'onVentilatorCumulative',
						'onVentilatorCurrently', 'positive']


			def get_absolute_url(self):
				return reverse("national-detail", kwargs={"id": self.id})

			def __str__(self):
				return "date: " + str(self.date) + "and number in icu: " + str(self.inIcuCumulative)

# class NationalTable(tables.Table):
# 	class Meta:
# 		model = National




class State(models.Model):
			date = models.DateField()
			state = models.CharField(max_length=2)
			death = models.IntegerField(default=0)
			hospitalizedCumulative = models.IntegerField(default=0)
			hospitalizedCurrently = models.IntegerField(default=0)
			inIcuCumulative = models.IntegerField(default=0)
			inIcuCurrently = models.IntegerField(default=0)
			negative = models.IntegerField(default=0)
			onVentilatorCumulative = models.IntegerField(default=0)
			onVentilatorCurrently = models.IntegerField(default=0)
			positive = models.IntegerField(default=0)

			class Meta:
				unique_together = ['state', 'date']



			@classmethod
			def get_expected_names(clas):
				return ['date', 'state', 'death', 'hospitalizedCumulative','hospitalizedCurrently', 'inIcuCumulative', 'inIcuCurrently', 'negative', 'onVentilatorCumulative',
						'onVentilatorCurrently', 'positive']



# class StateTable(tables.Table):
# 	class Meta:
# 		model = State















			
