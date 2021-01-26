from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

'''
each url is connected to a view, which is the http response
'''
app_name = 'dashboard'

urlpatterns = [
	#/dashboard/
	#path('', views.DashView.as_view(), name='dash'),
	path('upload-nation-csv/', views.national_data_upload, name='national_data_upload'),
	path('upload-state-csv/', views.state_data_upload, name='state_data_upload'),
	path('National/', views.NationalTableView.as_view(), name='national-List'),
	path('State/', views.StateTableView.as_view(), name='state-List'),
	path('National/<int:pk>/', views.NationalDetailView.as_view(), name='national-detail'),
	path('State/<int:pk>/', views.StateDetailView.as_view(), name='state-detail'),
	path('National/<int:pk>/update/', views.NationalUpdateView.as_view(), name='national-update'),
	path('State/<int:pk>/update', views.StateUpdateView.as_view(), name='state-update'),



	#/dashboard/id/
	#the () signifies that all the #s inside refer to one number ex (712) mean seven hundred and twelve, not 7,1,2

	#the ?P<...> takes the number passed in the url, lets say the id, makes it a variable that can be passed to the view function
	#the [0-9]+ means it can accept any number > 0
 
	#path('<int:pk>/', views.NationalDetailView, name='national-detail'),

]