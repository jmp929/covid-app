import django_filters as df
from .models import National

class NationalFilter(df.FilterSet):
	class Meta:
		model = National
		fields = {"date": ["exact", "contains"]}