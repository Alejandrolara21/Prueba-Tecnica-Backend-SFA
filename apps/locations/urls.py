from django.urls import path
from apps.locations.apiViews import *

urlpatterns = [
    path(r'apiListDepartment', api_list_department, name='apiListDepartment'),
    path(r'apiListDepartment/<int:pk>', api_list_department, name='apiListDepartment'),
	path(r'apiDepartment', api_department, name='apiDepartment'),
    path(r'apiDepartment/<int:pk>', api_department, name='apiDepartment'),

    path(r'apiListCity', api_list_city, name='apiListCity'),
    path(r'apiListCity/<int:pk>', api_list_city, name='apiListCity'),
    path(r'apiCity', api_city, name='apiCity'),
    path(r'apiCity/<int:pk>', api_city, name='apiCity'),

    path(r'apiListNeighborhood', api_list_neighborhood, name='apiListNeighborhood'),
    path(r'apiListNeighborhood/<int:pk>', api_list_neighborhood, name='apiListNeighborhood'),
    path(r'apiNeighborhood', api_neighborhood, name='apiNeighborhood'),
    path(r'apiNeighborhood/<int:pk>', api_neighborhood, name='apiNeighborhood'),

    path(r'apiListPollingPlace', api_list_polling_place, name='apiListPollingPlace'),
    path(r'apiListPollingPlace/<int:pk>', api_list_polling_place, name='apiListPollingPlace'),
    path(r'apiPollingPlace', api_polling_place, name='apiPollingPlace'),
    path(r'apiPollingPlace/<int:pk>', api_polling_place, name='apiPollingPlace'),
]