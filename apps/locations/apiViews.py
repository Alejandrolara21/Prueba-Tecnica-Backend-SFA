## propias
from apps.locations.models import *
from apps.locations.serializers import *

#librerias de restframework
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response

#librerias django
from django.db.models import Subquery,  OuterRef, Exists, Count, F, Q, Case, When

def show_info_api(data, status):
    showData = {}
    if(status == 200):
        showData = {
            'message':'success',
            'result':data,
        }
    else:
        showData = {
            'message':'error',
            'result':data,
        }
    return showData

@api_view(['GET','POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_department(request, pk=None):
    if(request.method == 'GET'):
        queryset = Department.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        queryset = queryset.annotate(state_name=F('state__name'))
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        data = request.data
        serializer = DepartmentSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            queryset = Department.objects.get(id=pk)
            data = request.data
            serializer = DepartmentSerializer(queryset, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)

@api_view(['GET','POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_city(request, pk=None):
    if(request.method == 'GET'):
        queryset = City.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        queryset = queryset.annotate(state_name=F('state__name'),department_name=F('department__name'))
        serializer = CitySerializer(queryset, many=True)        
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        data = request.data
        serializer = CitySerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            queryset = City.objects.get(id=pk)
            data = request.data
            serializer = CitySerializer(queryset, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)


@api_view(['GET','POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_neighborhood(request, pk=None):
    if(request.method == 'GET'):
        queryset = Neighborhood.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        queryset = queryset.annotate(state_name=F('state__name'),department_name=F('city__department__name'),city_name=F('city__name'))
        serializer = NeighborhoodSerializer(queryset, many=True)        
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        data = request.data
        serializer = NeighborhoodSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            queryset = Neighborhood.objects.get(id=pk)
            data = request.data
            serializer = NeighborhoodSerializer(queryset, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)


@api_view(['GET','POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_polling_place(request, pk=None):
    if(request.method == 'GET'):
        queryset = PollingPlace.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        queryset = queryset.annotate(state_name=F('state__name'),neighborhood_name=F('neighborhood__name'),department_name=F('neighborhood__city__department__name'),city_name=F('neighborhood__city__name'))
        serializer = PollingPlaceSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)
    elif(request.method == 'POST'):
        data = request.data
        serializer = PollingPlaceSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            queryset = PollingPlace.objects.get(id=pk)
            data = request.data
            serializer = PollingPlaceSerializer(queryset, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)