## propias
from users.models import *
from users.serializers import *
from locations.apiViews import show_info_api

#librerias de restframework
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response

#librerias django
from django.contrib.auth.hashers import make_password
from django.db.models import Subquery,  OuterRef, Exists, Count, F, Q, Case, When
from django.contrib.auth.models import User
from django.http import JsonResponse


@api_view(['GET','POST','PATCH'])
@permission_classes((AllowAny, ))
def api_user_admin(request):
    if(request.method == 'GET'):
        queryset = User.objects.filter(is_superuser=True)
        queryset = queryset.annotate(role_name=F('groups__name'),role=F('groups'))
        serializer = UserSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)


@api_view(['GET','POST','PATCH'])
def api_user_leader(request):
    if(request.method == 'GET'):
        queryset = Leader.objects.all()
        queryset = queryset.annotate(first_name=F('user__first_name'),last_name=F('user__last_name'),email=F('user__email'),document_type_name=F('document_type__name'))
        serializer = LeaderSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    elif(request.method == 'POST'):
        data = request.data
        data['password'] = make_password(data['password'])
        serializerUser = UserLeaderSerializer(data=data)
        if(serializerUser.is_valid()):
            print(serializerUser.validated_data)
            data['user'] = serializerUser.validated_data
            serializerLeader = LeaderSerializer(data=data)
            if(serializerLeader.is_valid()):
                serializerUser.save()
                serializerLeader.save()
                return Response(serializerLeader.data, status=201)
            else:
                return Response(serializerLeader.errors, status=400)
        else:
            return Response(serializerUser.errors, status=400)



@api_view(['GET','POST','PUT'])
def api_voter(request):
    if(request.method == 'GET'):
        queryset = Voter.objects.all()
        serializer = VoterSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        data = request.data
        data['state'] = State.objects.get(name="active").id
        data['leader'] = User.objects.get(id=request.user.id).id
        serializer = VoterSerializer(data=data)
        if(serializer.is_valid()):
            print(serializer.data['leader'])
            # serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)

        