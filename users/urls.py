from django.urls import path
from users.views import *
from users.apiViews import *

urlpatterns = [
	#---------apis APP ---------
	path(r'apiUserAdmin', api_user_admin, name='apiUserAdmin'),
    path(r'apiUserLeader', api_user_leader, name='apiUserLeader'),

	path(r'apiVoter', api_voter, name='apiVoter'),

]