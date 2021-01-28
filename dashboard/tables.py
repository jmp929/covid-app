import django_tables2 as tables
 
from .models import National, State
from django_tables2.utils import A


#Table for non users, no edit field given
class NationalTable(tables.Table):
	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = ['date',
			'death',
			'deathIncrease',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			]
		sequence = ('date',
			'death',
			'deathIncrease',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			)


#Table for non users, no edit field given
class StateTable(tables.Table):
	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		fields = ['date',
			'state',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			]
		sequence = ('date',
			'state',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			)

#Table for users only which displays the option to 'edit', meaning update or delete data
class NationalTableLI(tables.Table):
	
	edit = tables.columns.LinkColumn('dashboard:national-detail', text="edit", args=[A('pk')], orderable=False)


	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = ['date',
			'death',
			'deathIncrease',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			]
		sequence = ('date',
			'death',
			'deathIncrease',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			)




#Table for users only which displays the option to 'edit', meaning update or delete data
class StateTableLI(tables.Table):

	edit = tables.columns.LinkColumn('dashboard:state-detail', text="edit", args=[A('pk')], orderable=False)

	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		fields = ['date',
			'state',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			'edit',
			]
		sequence = ('date',
			'state',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'inIcuCurrently',
			'inIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			'edit'
			)













