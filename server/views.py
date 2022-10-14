from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import status, filters

from .models import Server
from .serializers import ServerSerializer


class ServerListView(ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # Получить VPS по UID
    search_fields = ['uid']
    # Получить список VPS с возможностью фильтрации по параметрам
    ordering_fields = ['cpu', 'ram', 'hdd', 'status']

    # Создать VPS
    def post(self, request, *args, **kwargs):
        data = {
            'cpu': request.data.get('cpu'), 
            'ram': request.data.get('ram'), 
            'hdd': request.data.get('hdd')
        }
        serializer = ServerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServerSingleView(RetrieveUpdateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def get_object(self, uid):
        try:
            return Server.objects.get(uid=uid)
        except Server.DoesNotExist:
            return None

    def get(self, request, uid, *args, **kwargs):
        server_instance = self.get_object(uid)
        if not server_instance:
            return Response(
                {"result": "VPS c такими UID не существует"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ServerSerializer(server_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Перевести VPS в другой статус
    def put(self, request, uid, *args, **kwargs):
        server_instance = self.get_object(uid)
        if not server_instance:
            return Response(
                {"result": "VPS c такими UID не существует"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'status': request.data.get('status')
        }
        serializer = ServerSerializer(instance=server_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
