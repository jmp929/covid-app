from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView, CreateView)
from django.views.generic.base import TemplateView
from .models import National, State
from .tables import NationalTable, StateTable, NationalTableLI, StateTableLI
from datetime import datetime
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import csv,  io
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import MultiTableMixin
from django.contrib import messages
from .filters import NationalFilter
from django.contrib.admin.views.decorators import staff_member_required


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
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'InIcuCurrently',
			'InIcuCumulative',
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
			'positive',
			'negative',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'InIcuCurrently',
			'InIcuCumulative',
			'onVentilatorCurrently',
			'onVentilatorCumulative',
			]

#@login_required
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


@permission_required('admin.can_add_log_entry')
def national_data_upload(request):

	context = {
		'data': 'upload the data here'
	}
	if request.method == "GET":
		return render(request, "dashboard/national_data_upload.html", context)


	tmp_file = request.FILES['file']

	if not tmp_file.name.endswith('.csv'):
		messages.error(request, "incorrect file type")

	data_set = tmp_file.read().decode('UTF-8')


	io_string = io.StringIO(data_set)
	next(io_string)

	for col in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, temp = National.objects.update_or_create(
			date = datetime.strptime(col[0], "%Y-%m-%d"),
			death = col[1],
			deathIncrease = col[2],
			InIcuCumulative = col[3],
			InIcuCurrently = col[4],
			hospitalizedIncrease = col[5],
			hospitalizedCurrently = col[6],
			hospitalizedCumulative = col[7],
			negative = col[8],
			negativeIncrease = col[9],
			onVentilatorCumulative = col[10],
			onVentilatorCurrently = col[11],
			positive = col[12],
			positiveIncrease = col[13],
			states = col[14],
			totalTestResults = col[15],
			totalTestResultsIncrease = col[16],
			)
	context = {}
	return render(request, "dashboard/national_data_upload.html", context)


@permission_required('admin.can_add_log_entry')
def state_data_upload(request):

	context = {
		'data': 'upload the data here'
	}

	if request.method == "GET":
		return render(request, "dashboard/national_data_upload.html", context)


	tmp_file = request.FILES['file']

	if not tmp_file.name.endswith('.csv'):
		messages.error(request, "not right")

	data_set = tmp_file.read().decode('UTF-8')
	

	io_string = io.StringIO(data_set)
	next(io_string)

	for col in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, temp = State.objects.update_or_create(
			date = datetime.strptime(col[0], "%Y-%m-%d"),
			state = col[1],
			dataQualityGrade = col[2],
			death = int(float(col[3])),
			deathConfirmed = int(float(col[4])),
			deathIncrease = int(float(col[5])),
			deathProbable = int(float(col[6])),
			hospitalized = int(float(col[7])),
			hospitalizedCumulative = int(float(col[8])),
			hospitalizedCurrently = int(float(col[9])),
			hospitalizedIncrease = int(float(col[10])),
			inIcuCumulative = int(float(col[11])),
			inIcuCurrently = int(float(col[12])),
			negative = int(float(col[13])),
			negativeIncrease = int(float(col[14])),
			negativeTestsAntibody = int(float(col[15])),
			negativeTestsPeopleAntibody = int(float(col[16])),
			negativeTestsViral = int(float(col[17])),	
			onVentilatorCumulative = int(float(col[18])),
			onVentilatorCurrently = int(float(col[19])),	
			positive = int(float(col[20])),	
			positiveCasesViral = int(float(col[21])),	
			positiveIncrease = int(float(col[22])),	
			positiveScore = int(float(col[23])),	
			positiveTestsAntibody = int(float(col[24])),	
			positiveTestsAntigen = int(float(col[25])),	
			positiveTestsPeopleAntibody = int(float(col[26])),	
			positiveTestsPeopleAntigen = int(float(col[27])),	
			positiveTestsViral = int(float(col[28])),	
			recovered = int(float(col[29])),
			totalTestEncountersViral = int(float(col[30])),	
			totalTestEncountersViralIncrease = int(float(col[31])),	
			totalTestResults = int(float(col[32])),	
			totalTestResultsIncrease = int(float(col[33])),	
			totalTestsAntibody = int(float(col[34])),	
			totalTestsAntigen = int(float(col[35])),	
			totalTestsPeopleAntibody = int(float(col[36])),	
			totalTestsPeopleAntigen = int(float(col[37])),	
			totalTestsPeopleViral = int(float(col[38])),	
			totalTestsPeopleViralIncrease = int(float(col[39])),	
			totalTestsViral = int(float(col[40])),	
			totalTestsViralIncrease = int(float(col[41])),
			)

	context = {}
	return render(request, "dashboard/state_data_upload.html", context)
