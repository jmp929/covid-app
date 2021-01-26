from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView, CreateView)
from .models import National, State
from .tables import NationalTable, StateTable, NationalTableLI, StateTableLI
from datetime import datetime
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import csv,  io
from django_tables2 import SingleTableView
from django_tables2.views import MultiTableMixin
from django.contrib import messages


class DashView(MultiTableMixin):
	template_name = 'dashboard/dash.html'

	query1 = National.objects.all()
	query2 = State.objects.all()

	tables = [
		NationalTable(query1),
		StateTable(query2)
	]

class NationalTableView(SingleTableView):
	model = National
	template_name = "dashboard/national_list.html"
	table_class = NationalTable
	# def get_table_class(self):
	# 	if self.request.user.is_authenticated:
	# 		print("not here")
	# 		return NationalTableLI
	# 	else:
	# 		print("here")
	# 		return NationalTable


class StateTableView(SingleTableView):
	table_class = StateTable

	model = State
	template_name = "dashboard/state_list.html"

class NationalDetailView(LoginRequiredMixin, DetailView):
	login_url = '/login/'
	redirect_field_name = 'login'
	table_class = NationalTable
	model = National
	template_name = "dashboard/national_detail.html"

class StateDetailView(LoginRequiredMixin, DetailView):
	login_url = '/login/'
	redirect_field_name = 'login'
	table_class = StateTable
	model = State
	template_name = "dashboard/state_detail.html"


class NationalUpdateView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	redirect_field_name = 'login'
	model = National
	template_name = "dashboard/national_update.html"

	fields = ['date',
			'death',
			'deathIncrease',
			'InIcuCumulative',
			'InIcuCurrently',
			'hospitalizedIncrease',
			'hospitalizedCurrently',
			'hospitalizedCumulative',
			'negative',
			'negativeIncrease',
			'onVentilatorCumulative',
			'onVentilatorCurrently',
			'positive',
			'positiveIncrease',
			'states',
			'totalTestResults',
			'totalTestResultsIncrease',
			]	

#@login_required
class StateUpdateView(LoginRequiredMixin, UpdateView):
	model = State
	template_name = "dashboard/state_update.html"
	
	fields = ["date",
			"state",
			"dataQualityGrade",
			"death",
			"deathConfirmed",
			"deathIncrease",
			"deathProbable",
			"hospitalized",
			"hospitalizedCumulative",
			"hospitalizedCurrently",
			"hospitalizedIncrease",
			"inIcuCumulative",
			"inIcuCurrently",
			"negative",
			"negativeIncrease",
			"negativeTestsAntibody",
			"negativeTestsPeopleAntibody",
			"negativeTestsViral",
			"onVentilatorCumulative",
			"onVentilatorCurrently",
			"positive",
			"positiveCasesViral", 	
			"positiveIncrease", 	
			"positiveScore", 
			"positiveTestsAntibody", 
			"positiveTestsAntigen", 	
			"positiveTestsPeopleAntibody",	
			"positiveTestsPeopleAntigen", 	
			"positiveTestsViral", 	
			"recovered",
			"totalTestEncountersViral", 	
			"totalTestEncountersViralIncrease", 	
			"totalTestResults", 	
			"totalTestResultsIncrease", 	
			"totalTestsAntibody", 	
			"totalTestsAntigen", 
			"totalTestsPeopleAntibody", 
			"totalTestsPeopleAntigen", 	
			"totalTestsPeopleViral", 	
			"totalTestsPeopleViralIncrease", 	
			"totalTestsViral", 	
			"totalTestsViralIncrease"
			]













@permission_required('admin.can_add_log_entry')
def national_data_upload(request):

	context = {
		'data': 'upload the data here'
	}

	if request.method == "GET":
		return render(request, "dashboard/national_data_upload.html", context)


	prik = request.FILES['file']

	if not prik.name.endswith('.csv'):
		messages.error(request, "incorrect file type")

	data_set = prik.read().decode('UTF-8')
	

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


	prik = request.FILES['file']

	if not prik.name.endswith('.csv'):
		messages.error(request, "not right")

	data_set = prik.read().decode('UTF-8')
	

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






# class NationalListView(ListView):
# 	model = National
# 	template_name = "national_list.html"
# 	context_name = "national_list"
# 	paginate_by = 100


# class StateListView(ListView):
# 	model = State
# 	template_name = "state_list.html"
# 	context_name = "state_list"
# 	paginate_by = 100

# 	def query_set(self):
# 		queryset = State.objects




# from django.views import generic
# from django.core import Paginator
# from django.shortcuts import get_object_or_404, render, redirect
# from .models import National, State



# def NationalListView(request):
# 	nationalQuery = National.objects.all()
# 	pag = Paginator(nationalQuery, 25)

# 	page = request.GET.get('page')


# 	return render(request, "dashboard/national_list_view.html", {"nationalQuery": nationalQuery})

# def NationalDetailView(request, pk):
# 	nationalQuery = get_object_or_404(National, pk=pk)

# 	return render(request, "dashboard/national_detail_view.html", {"national_day": nationalQuery})

# def stateListView(request):
# 	stateQuery = State.objects.all()

# 	return render(request, "dashboard/state_list_view.html", {"stateQuery": stateQuery})

# def stateDetailView(request, pk):
# 	stateQuery = get_object_or_404(State, pk=pk)

# 	return render(request, "dashboard/state_detail_view.html", {"state_day": stateQuery})




























'''
views is what sends back the http response to the client when they look up the url
and when they use the page. The view handles the requests from the client

request - wants http response
'''

# def index(request):
# 	all_national = National.objects.all()
# 	context = {
# 		'all_national': all_national,
# 	}
# 	return render(request, "dashboard/index.html", context)

# def detail(request, national_id):

# 	national = get_object_or_404(National, id=national_id)
	
# 	return render(request, "dashboard/detail.html", {"national": national})
