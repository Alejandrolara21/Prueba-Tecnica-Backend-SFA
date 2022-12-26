from django.urls import path
from states.apiViews import *

urlpatterns = [
	path(r'apiState', api_state, name='apiState'),
]