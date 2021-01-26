import django_tables2 as tables
from .models import National, State
from django_tables2.utils import A


class NationalTable(tables.Table):
	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'death', 'InIcuCurrently', 'positive', 'detail'}
		sequence = ('id', 'date', 'death', 'InIcuCurrently', 'positive', 'detail')
		#edit = TemplateColumn(template_name='dashboard/national_list')



class StateTable(tables.Table):
	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'state', 'death', 'positive'}
		sequence = ('id', 'date', 'state', 'death', 'positive')
		#edit = TemplateColumn(template_name='dashboard/national_list')


class NationalTableLI(tables.Table):
	
	detail = tables.columns.LinkColumn('national-detail', text='static text', args=[A('id')], orderable=False, empty_values=())


	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'death', 'InIcuCurrently', 'positive', 'detail'}
		sequence = ('id', 'date', 'death', 'InIcuCurrently', 'positive', 'detail')
		#edit = TemplateColumn(template_name='dashboard/national_list')

	


class StateTableLI(tables.Table):

	detail = tables.columns.LinkColumn('state_detail', args=[A('pk')])

	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'state', 'death', 'positive'}
		sequence = ('id', 'date', 'state', 'death', 'positive')
		#edit = TemplateColumn(template_name='dashboard/national_list')