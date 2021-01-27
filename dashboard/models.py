from django.db import models
from django.urls import reverse
import django_tables2 as tables

class National(models.Model):
			date = models.DateField(unique=True, max_length=11)
			death = models.IntegerField(default=0, max_length=11)
			InIcuCumulative = models.IntegerField(default=0, max_length=11)
			InIcuCurrently = models.IntegerField(default=0, max_length=11)
			hospitalizedCurrently = models.IntegerField(default=0, max_length=11)
			hospitalizedCumulative = models.IntegerField(default=0, max_length=11)
			negative = models.IntegerField(default=0, max_length=11)
			onVentilatorCumulative = models.IntegerField(default=0, max_length=11)
			onVentilatorCurrently = models.IntegerField(default=0, max_length=11)
			positive = models.IntegerField(default=0, max_length=11)


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



# class StateTable(tables.Table):
# 	class Meta:
# 		model = State















			
