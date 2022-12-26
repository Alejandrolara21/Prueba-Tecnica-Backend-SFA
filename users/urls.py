from django.urls import path
from users.views import *
from users.apiViews import *

urlpatterns = [
	#---------apis APP ---------
	path(r'login', login_user, name='login'),
	path(r'logout', logout_user, name='logout'),
	path(r'apiDocumentType', api_document_type, name='apiDocumentType'),
	path(r'apiDocumentType/<int:pk>', api_document_type, name='apiDocumentType'),

	path(r'apiUser', api_user, name='apiUser'),
	path(r'apiUser/<int:pk>', api_user, name='apiUser'),
    path(r'apiUserLeader', api_user_leader, name='apiUserLeader'),
	path(r'apiUserLeader/<int:pk>', api_user_leader, name='apiUserLeader'),

	path(r'apiVoter', api_voter, name='apiVoter'),
	path(r'apiVoter/<int:pk>', api_voter, name='apiVoter'),

	path(r'apiStatistics', api_statistics, name='apiStatistics'),

]