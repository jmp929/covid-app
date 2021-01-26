import django_tables2 as tables
 
from .models import National, State
from django_tables2.utils import A


class NationalTable(tables.Table):
	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		attrs = {'class': 'national_table', 'div': 'hdr'}
		fields = ['date',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'InIcuCurrently',
			'InIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			]
		sequence = ('date',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'InIcuCurrently',
			'InIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			)



class StateTable(tables.Table):
	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		attrs = {'class': 'state_table', 'div': 'body'}
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


class NationalTableLI(tables.Table):
	
	edit = tables.columns.LinkColumn('dashboard:national-detail', text="edit", args=[A('pk')], orderable=False)


	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = ['date',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'InIcuCurrently',
			'InIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			]
		sequence = ('date',
			'death',
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'InIcuCurrently',
			'InIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			)





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













