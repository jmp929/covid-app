from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

'''
each url is connected to a view, which is the http response
'''
app_name = 'dashboard'

urlpatterns = [
	#/dashboard/
	path('', views.DashboardView.as_view(), name='dash'),
	path('upload-nation-csv/', views.national_data_upload, name='national_data_upload'),
	path('upload-state-csv/', views.state_data_upload, name='state_data_upload'),
	path('National/', views.NationalTableView.as_view(), name='national-List'),
	path('State/', views.StateTableView.as_view(), name='state-List'),
	path('National/<int:pk>/', views.NationalDetailView.as_view(), name="national-detail"),
	path('State/<int:pk>/', views.StateDetailView.as_view(), name='state-detail'),
	path('National/<int:pk>/update/', views.NationalUpdateView.as_view(), name='national-update'),
	path('State/<int:pk>/update/', views.StateUpdateView.as_view(), name='state-update'),
	path('National/create/', views.NationalCreateView.as_view(), name='national-create'),
	path('State/create/', views.StateCreateView.as_view(), name='state-create'),
	path('National/<int:pk>/delete/', views.NationalDeleteView.as_view(), name='national-delete'),
	path('State/<int:pk>/delete/', views.StateDeleteView.as_view(), name='state-delete'),
	
	path('donations/', views.DonationsView, name='donations'),

	path('api/statechart1/data', views.StateChartData1.as_view(), name='api-statechart1-data'),
	path('api/nationalchart1/data', views.NationalChartData1.as_view(), name='api-nationalchart1-data'),
	path('api/statechart2/data', views.StateChartData2.as_view(), name='api-statechart2-data'),
	path('api/nationalchart2/data', views.NationalChartData2.as_view(), name='api-nationalchart2-data'),


]