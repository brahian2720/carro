from rest_framework import viewsets, permissions
from .models import Marca, Car, Dueño, DueñoCar
from .serializer import MarcaSerializer, DueñoSerializer, CarSerializer, DueñoCarSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class DueñoViewSet(viewsets.ModelViewSet):
    serializer_class = DueñoSerializer
    queryset = Dueño.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class CarViewSet(viewsets.ModelViewSet): 
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class DueñoCarViewSet(viewsets.ModelViewSet): 
    serializer_class = DueñoCarSerializer
    queryset = DueñoCar.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
