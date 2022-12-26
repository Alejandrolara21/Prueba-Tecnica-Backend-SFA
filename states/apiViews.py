## propias
from states.models import *
from states.serializers import *

#librerias de restframework
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response


@api_view(['GET'])
def api_state(request):
    if(request.method == 'GET'):
        queryset = State.objects.all()
        serializer = StateSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)