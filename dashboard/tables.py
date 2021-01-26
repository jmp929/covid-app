import django_tables2 as tables
 
from .models import National, State
from django_tables2.utils import A


class NationalTable(tables.Table):
	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'death', 'InIcuCurrently', 'positive'}
		sequence = ('id', 'date', 'death', 'InIcuCurrently', 'positive')
		#edit = TemplateColumn(template_name='dashboard/national_list')



class StateTable(tables.Table):
	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'state', 'death', 'positive'}
		sequence = ('id', 'date', 'state', 'death', 'positive')
		#edit = TemplateColumn(template_name='dashboard/national_list')


class NationalTableLI(tables.Table):
	
	edit = tables.columns.LinkColumn('dashboard:national-detail', text="edit", args=[A('pk')], orderable=False)


	class Meta:
		model = National
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'death', 'InIcuCurrently', 'positive', 'edit'}
		sequence = ('id', 'date', 'death', 'InIcuCurrently', 'positive', 'edit')
		#edit = TemplateColumn(template_name='dashboard/national_list')

	


class StateTableLI(tables.Table):

	detail = tables.columns.LinkColumn('state_detail', args=[A('pk')])

	class Meta:
		model = State
		template_name = "django_tables2/bootstrap4.html"
		fields = {'id', 'date', 'state', 'death', 'positive'}
		sequence = ('id', 'date', 'state', 'death', 'positive')
		#edit = TemplateColumn(template_name='dashboard/national_list')