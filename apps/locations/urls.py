from django.urls import path
from apps.locations.apiViews import *

urlpatterns = [
	path(r'apiDepartment', api_department, name='apiDepartment'),
    path(r'apiDepartment/<int:pk>', api_department, name='apiDepartment'),
    path(r'apiCity', api_city, name='apiCity'),
    path(r'apiCity/<int:pk>', api_city, name='apiCity'),
    path(r'apiNeighborhood', api_neighborhood, name='apiNeighborhood'),
    path(r'apiNeighborhood/<int:pk>', api_neighborhood, name='apiNeighborhood'),
    path(r'apiPollingPlace', api_polling_place, name='apiPollingPlace'),
    path(r'apiPollingPlace/<int:pk>', api_polling_place, name='apiPollingPlace'),
]