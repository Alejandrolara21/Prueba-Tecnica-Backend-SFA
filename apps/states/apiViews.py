## propias
from apps.states.models import *
from apps.states.serializers import *
from apps.locations.apiViews import show_info_api

#librerias de restframework
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_list_state(request, pk=None):
    if(request.method == 'GET'):
        queryset = State.objects.all()
        if(pk):
            queryset = queryset.filter(id=pk)
        serializer = StateSerializer(queryset, many=True)
        return Response(show_info_api(serializer.data,200), status=200)

@api_view(['POST','PUT'])
@permission_classes((IsAdminUser, ))
def api_state(request, pk=None):
    if(request.method == 'POST'):
        data = request.data
        serializer = StateSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(show_info_api(serializer.data,200), status=200)
        else:
            return Response(show_info_api(serializer.errors,400), status=400)
    elif(request.method == 'PUT'):
        if pk:
            queryset = State.objects.get(id=pk)
            data = request.data
            serializer = StateSerializer(queryset, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(show_info_api(serializer.data,200), status=200)
            else:
                return Response(show_info_api(serializer.errors,400), status=400)
        else:
            return Response(show_info_api({"id":["This field is required in the URL."]},400), status=400)
