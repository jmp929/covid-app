from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView, CreateView)
from .models import National, State
from .tables import NationalTable, StateTable, NationalTableLI, StateTableLI
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
import csv,  io
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import MultiTableMixin
from django.contrib import messages
from .filters import NationalFilter
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.db.models import Sum, Max



class DonationsView(SingleTableView):
	template_name = 'dashboard/donations.html'
	model = National
	table_class = NationalTable


class DashboardView(SingleTableView):
	template_name = 'dashboard/dash.html'
	model = National
	table_class = NationalTable


class DashboardExtView(SingleTableView):
	template_name = 'dashboard/dash_ext.html'
	model = State
	table_class = NationalTable


class NationalTableView(SingleTableView, FilterView):
	model = National
	template_name = "dashboard/national_list.html"

	filter_class = NationalFilter
	#only give users the option to see the details of the data, and thus update or delete
	def get_table_class(self):
		if self.request.user.is_authenticated:
			print("not here")
			return NationalTableLI
		else:
			print("here")
			return NationalTable


class StateTableView(SingleTableView):
	table_class = StateTable

	model = State
	template_name = "dashboard/state_list.html"
	#only give users the option to see the details of the data, and thus update or delete
	def get_table_class(self):
		if self.request.user.is_authenticated:
			print("not here")
			return StateTableLI
		else:
			print("here")
			return StateTable

class NationalDetailView(LoginRequiredMixin, DetailView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = National
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
	template_name = "dashboard/national_detail.html"

class StateDetailView(LoginRequiredMixin, DetailView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = State
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
	template_name = "dashboard/state_detail.html"


class NationalDeleteView(LoginRequiredMixin, DeleteView):
	login_url = '/login/'
	redirect_field_name = 'login'
	success_url = reverse_lazy('dashboard:national-List')
	model = National
	template_name = "dashboard/national_delete.html"

class StateDeleteView(LoginRequiredMixin, DeleteView):
	login_url = '/login/'
	redirect_field_name = 'login'
	success_url = reverse_lazy('dashboard:state-List')
	model = State
	template_name = "dashboard/state_delete.html"

class NationalCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = National
	success_url = reverse_lazy('dashboard:national-List')
	template_name = "dashboard/national_create.html"
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

class StateCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = State
	success_url = reverse_lazy('dashboard:state-List')
	template_name = "dashboard/national_create.html"
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


class NationalUpdateView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = National
	success_url = reverse_lazy('dashboard:national-List')
	template_name = "dashboard/national_update.html"

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


class StateUpdateView(LoginRequiredMixin, UpdateView):
	model = State
	template_name = "dashboard/state_update.html"
	success_url = reverse_lazy('dashboard:state-List')
	fields = ['date',
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

#Give only admin users the ability to upload a new CSV
@permission_required('admin.can_add_log_entry')
def national_data_upload(request):

	context = {
		'data': 'upload the data here'
	}

	no_errors = True
	if request.method == "GET":
		return render(request, "dashboard/national_data_upload.html", context)


	tmp_file = request.FILES['file']

	#verify the file is CSV format
	if no_errors:
		if not tmp_file.name.endswith('.csv'):
			no_errors = False
			messages.error(request, "incorrect file type")

	data_set = tmp_file.read().decode('UTF-8')


	io_string = io.StringIO(data_set)

	new_names = []
	for row in csv.reader(io_string, delimiter = ',') : 
		new_names.extend(row) 
		break


	expected_names = National.get_expected_names()
	#verifying CSV file is correct length
	if no_errors:
		if (len(expected_names) != len(new_names)):
			no_errors = False
			messages.error(request, "incorrect CSV size")

	#verifying CSV file matches proper table headings
	if no_errors:
		for x in range(len(expected_names)):
			if (expected_names[x] != new_names[x]):
				no_errors = False
				messages.error(request, "incorrect CSV data")
				break


	


	next(io_string)


	if no_errors:
		for col in csv.reader(io_string, delimiter=',', quotechar="|"):
			_, temp = National.objects.update_or_create(
				date = datetime.strptime(col[0], "%Y-%m-%d"),
				death = int(float(col[1])),
				deathIncrease = int(float(col[2])),
				inIcuCumulative = int(float(col[3])),
				inIcuCurrently = int(float(col[4])),
				hospitalizedCurrently = int(float(col[5])),
				hospitalizedCumulative = int(float(col[6])),
				negative = int(float(col[7])),
				onVentilatorCumulative = int(float(col[8])),
				onVentilatorCurrently = int(float(col[9])),
				positive = int(float(col[10])),
				)
	context = {}
	return render(request, "dashboard/national_data_upload.html", context)

#Give only admin users the ability to upload a new CSV
@permission_required('admin.can_add_log_entry')
def state_data_upload(request):

	context = {
		'data': 'upload the data here'
	}
	no_errors=True
	if request.method == "GET":
		return render(request, "dashboard/national_data_upload.html", context)


	tmp_file = request.FILES['file']
	#verify the file is CSV format
	if not tmp_file.name.endswith('.csv'):
		messages.error(request, "not right")

	data_set = tmp_file.read().decode('UTF-8')
	

	io_string = io.StringIO(data_set)

	new_names = []
	for row in csv.reader(io_string, delimiter = ',') : 
		new_names.extend(row) 
		break


	expected_names = National.get_expected_names()
	#verifying CSV file is correct length
	if no_errors:
		if (len(expected_names) != len(new_names)):
			no_errors = False
			messages.error(request, "incorrect CSV size")

	#verifying CSV file matches proper table headings
	if no_errors:
		for x in range(len(expected_names)):
			if (expected_names[x] != new_names[x]):
				no_errors = False
				messages.error(request, "incorrect CSV data")
				break



	next(io_string)

	if no_errors:
		for col in csv.reader(io_string, delimiter=',', quotechar="|"):
			_, temp = State.objects.update_or_create(
				date = datetime.strptime(col[0], "%Y-%m-%d"),
				state = col[1],
				death = int(float(col[2])),
				hospitalizedCumulative = int(float(col[3])),
				hospitalizedCurrently = int(float(col[4])),
				inIcuCumulative = int(float(col[5])),
				inIcuCurrently = int(float(col[6])),
				negative = int(float(col[7])),
				onVentilatorCumulative = int(float(col[8])),
				onVentilatorCurrently = int(float(col[9])),	
				positive = int(float(col[10])),	
				)

	context = {}
	return render(request, "dashboard/state_data_upload.html", context)




#Render data for chart of deaths per state
class StateChartData(APIView): 
	authentication_classes = [] 
	permission_classes = [] 
   
	def get(self, request, format = None): 
		labelsView = []
		dataView = []

		queryset = State.objects.values('state').annotate(max_deaths=Max('death')).order_by('-max_deaths')
		for entry in queryset:
			print(entry)
			labelsView.append(entry['state'])
			dataView.append(entry['max_deaths'])

		chartLabel = "Chart of Deaths by State"
		data = {
			'labelsView': labelsView,
			'dataView': dataView,
			'chartLabel': chartLabel,
		}
		return Response(data)
  



#Render data for top 50 most deadly days in the US 
class NationalChartData(APIView): 
	authentication_classes = [] 
	permission_classes = [] 
   
	def get(self, request, format = None): 
		labelsView = []
		dataView = []
		queryset = National.objects.all().order_by('-deathIncrease')[:50]

		for entry in queryset:
			print(entry)
			labelsView.append(entry.__dict__['date'])
			dataView.append(entry.__dict__['deathIncrease'])
		
			

		chartLabel = "Chart of Deaths Nationally by Day"
		data = {
			'labelsView': labelsView,
			'dataView': dataView,
			'chartLabel': chartLabel,
		}
		return Response(data)
























