## propias
from apps.users.models import *
from apps.users.serializers import *
from apps.locations.apiViews import show_info_api

#librerias de restframework
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

#librerias django
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Subquery,  OuterRef, Exists, Count, F, Q, Case, When
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import os


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    email = data['email']
    password = data['password']
    try:
        account = User.objects.get(email=email)
    except BaseException as e:
        return Response(show_info_api({"message": str(e)},400), status=400)

    token = Token.objects.get_or_create(user=account)[0].key
    if not check_password(password, account.password):
        return Response(show_info_api({"message": "Incorrect Login credentials"},400), status=400)

    if account:
        if account.is_active:
            login(request, account)
            return Response(show_info_api({"email": account.email, "token": token},200), status=200)
        else:
            return Response(show_info_api({"message": "Account not active"},400), status=400)
    else:
        return Response(show_info_api({"message": "Account does not exist"},400), status=400)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    logout(request)
    return Response(show_info_api({"message": 'User Logged out successfully'},200), status=200)

@api_view(['GET','POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_document_type(request, pk=None):
    if(request.method == 'GET'):
        queryset = DocumentType.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        serializer = DocumentTypeSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        data = request.data
        serializer = DocumentTypeSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            queryset = DocumentType.objects.get(id=pk)
            data = request.data
            serializer = DocumentTypeSerializer(queryset, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)


@api_view(['GET','POST','PUT'])
@permission_classes((AllowAny, ))
def api_user(request, pk=None):
    if(request.method == 'GET'):
        queryset = User.objects.filter(groups__name='leader')
        if(pk):
            queryset = queryset.filter(id=pk)
        queryset = queryset.annotate(role_name=F('groups__name'),role=F('groups'))
        serializer = UserSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        request.data._mutable = True
        data = request.data
        data['password'] = make_password(data['password'])
        data['email'] = data['username'].lower()
        data['is_active'] =  bool(int(data['state']))
        data['role'] = Group.objects.get(name="leader").id
        serializer = UserCreateSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            user = User.objects.get(username=data['username'])
            user.groups.add(data['role'])
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            request.data._mutable = True
            data = request.data
            data['password'] = make_password(data['password'])
            data['email'] = data['username'].lower()
            data['is_active'] =  bool(int(data['state']))

            queryset = User.objects.get(id=pk)
            serializer = UserCreateSerializer(queryset, data=data, partial=True)
            if(serializer.is_valid()):
                serializer.save()
                user = User.objects.get(username=data['username'])
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)

@api_view(['GET','POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_user_leader(request, pk=None):
    if(request.method == 'GET'):
        queryset = Leader.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        queryset = queryset.annotate(first_name=F('user__first_name'),last_name=F('user__last_name'),email=F('user__email'),document_type_name=F('document_type__name'),state=F('user__is_active'))
        serializer = LeaderSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    
    elif(request.method == 'POST'):
        data = request.data
        serializer = LeaderSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    
    elif(request.method == 'PUT'):
        if pk:
            queryset = Leader.objects.get(user_id=pk)
            if(queryset.image):
                old_file = str(queryset.image)
            
            serializer = LeaderSerializer(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                if(serializer.data['image']):
                    if(old_file):
                        file_path = settings.MEDIA_ROOT+'/'+old_file
                        if(os.path.isfile(file_path)):
                            os.remove(file_path)
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)


@api_view(['GET','POST','PUT'])
@permission_classes([IsAuthenticated])
def api_voter(request,pk=None):
    if(request.method == 'GET'):
        queryset = Voter.objects.all()
        if(not request.user.is_superuser):
            queryset = queryset.filter(leader=request.user.id)
        
        if(request.user.is_superuser and pk):
            queryset = queryset.filter(id=pk)
        serializer = VoterSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        if(not request.user.is_superuser):
            request.data._mutable = True
            data = request.data
            data['leader'] = request.user.id
            serializer = VoterSerializer(data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"Only leader can Create and Update Voters"},400), status=400)   
    elif(request.method == 'PUT'):
        if(not request.user.is_superuser):
            if pk:
                queryset = Voter.objects.get(id=pk)
                if(request.user.id == queryset.leader.user.id):
                    request.data._mutable = True
                    data = request.data
                    data['leader'] = request.user.id
                    serializer = VoterSerializer(queryset,data=data,partial=True)
                    if(serializer.is_valid()):
                        serializer.save()
                        return Response(show_info_api(serializer.data,200), status=200)
                    else:
                        return Response(show_info_api(serializer.errors,400), status=400)
                else:
                    return Response(show_info_api({"You can not update this voter."},400), status=400)
            else:
                return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)
        else:
            return Response(show_info_api({"Only leader can Create and Update Voters"},400), status=400)

@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def api_log_voter(request, pk=None):
    if(request.method == 'GET'):
        if pk:
            queryset = Log.objects.filter(voter__id=pk)
            serializer = LogSerializer(queryset, many=True)
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)

@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def api_statistics(request):
    if(request.method == 'GET'):
        queryset = Voter.objects.all()
        
        if(request.query_params.get('leader_id') != None):
            queryset = queryset.filter(leader__user__id=request.query_params.get('leader_id'))
        
        elif(request.query_params.get('city_id') != None):
            queryset = queryset.filter(polling_place__neighborhood__city=request.query_params.get('city_id'))
        
        elif(request.query_params.get('polling_place_id') != None and request.query_params.get('n_polling_station') != None):
            queryset = queryset.filter(Q(polling_place__id=request.query_params.get('polling_place_id'))&Q(polling_station=int(request.query_params.get('n_polling_station'))))
        

        count_data = queryset.count()
        serializer = VoterSerializer(queryset, many=True)
        return Response(show_info_api({"data":serializer.data,"count":count_data},200), status=200)