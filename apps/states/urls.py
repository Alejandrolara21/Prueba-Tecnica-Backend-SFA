from django.urls import path
from apps.states.apiViews import *

urlpatterns = [
	path(r'apiListState', api_list_state, name='apiListState'),
	path(r'apiListState/<int:pk>', api_list_state, name='apiListState'),
	path(r'apiState', api_state, name='apiState'),
	path(r'apiState/<int:pk>', api_state, name='apiState'),
]